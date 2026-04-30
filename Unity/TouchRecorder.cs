using System;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;
using TMPro;

/// <summary>
/// 单个命中节点的原始信息，由 Python 端 node_scorer 评分。
/// 字段命名与 Auto_test cocos/TouchRecorder.ts 保持一致，
/// 仅 components 改为 Unity 类名（Button/Toggle/TMP_InputField 等）。
/// </summary>
public class HitNodeInfo
{
    public string path;
    public string name;
    public List<string> components;
    public int depth;
    public float area;
    public bool? interactable;
    public float[] position;
    public float[] size;
    public int render_order;
    public List<ParentChainEntry> parent_chain;
    public bool? is_3d;
    public string locator_camera;
}

public class ParentChainEntry
{
    public string name;
    public string path;
    public List<string> components;
    public float[] position;
    public float[] size;
}

/// <summary>
/// 录制事件结构，对应 Python 端 recorder_server 的 record_event。
/// action 取值: click | swipe | input_text | ping
/// 坐标统一为 [0,1] 归一化、y 向下。
/// </summary>
public class RecordEvent
{
    public string action;
    public float[] position;
    public List<HitNodeInfo> hit_nodes;
    public float[] end_position;
    public double? duration;
    public string text;
    public long timestamp_ms;
}

/// <summary>
/// 触摸录制器。挂在 WSClientForTest 同一 GameObject 上，
/// 通过 Update() 轮询 Input + EventSystem.RaycastAll / Physics.RaycastAll 收集 hit_nodes，
/// 再以 record_event push 形式推回 Python。
/// </summary>
public class TouchRecorder : MonoBehaviour
{
    private const float SWIPE_THRESHOLD_PX = 30f;

    private bool isRecording;
    private Action<object> sendFn;
    private List<CameraConfigEntry> cameraConfigList = new List<CameraConfigEntry>();
    private long recordingStartTimeMs;

    private Vector2? downPos;
    private long downTimeMs;
    private enum InputSource { None, Mouse, Touch }
    private InputSource activeSource = InputSource.None;
    private int activeTouchFingerId = -1;

    private GameObject lastSelectedGo;
    private List<HitNodeInfo> pendingEditBoxHitNodes;
    private float[] pendingClickPosition;

    private bool _cam3DWarnLogged;

    public void Configure(Action<object> sendCallback)
    {
        sendFn = sendCallback;
    }

    public void SetCameraConfigList(List<CameraConfigEntry> list)
    {
        cameraConfigList = list != null ? new List<CameraConfigEntry>(list) : new List<CameraConfigEntry>();
    }

    public bool StartRecording()
    {
        if (isRecording) return false;
        if (sendFn == null)
        {
            Debug.LogError("[TouchRecorder] sendFn 未配置，无法启动录制");
            return false;
        }

        isRecording = true;
        recordingStartTimeMs = NowMs();
        downPos = null;
        activeSource = InputSource.None;
        activeTouchFingerId = -1;
        lastSelectedGo = null;
        pendingEditBoxHitNodes = null;
        pendingClickPosition = null;
        _cam3DWarnLogged = false;

        Debug.Log("[TouchRecorder] Recording started");

        SendRecordEvent(new RecordEvent
        {
            action = "ping",
            position = new float[] { 0f, 0f },
            timestamp_ms = 0,
        });
        return true;
    }

    public bool StopRecording()
    {
        if (!isRecording) return false;
        isRecording = false;
        downPos = null;
        activeSource = InputSource.None;
        activeTouchFingerId = -1;
        lastSelectedGo = null;
        pendingEditBoxHitNodes = null;
        pendingClickPosition = null;
        Debug.Log("[TouchRecorder] Recording stopped");
        return true;
    }

    void Update()
    {
        if (!isRecording) return;

        TrackInputFieldSelectionChange();
        PollMouse();
        PollTouches();
    }

    // ======================== 输入轮询 ========================

    private void PollMouse()
    {
        if (activeSource == InputSource.Touch) return;

        if (Input.GetMouseButtonDown(0))
        {
            activeSource = InputSource.Mouse;
            downPos = new Vector2(Input.mousePosition.x, Input.mousePosition.y);
            downTimeMs = NowMs();
        }
        if (Input.GetMouseButtonUp(0) && activeSource == InputSource.Mouse)
        {
            ProcessUp(new Vector2(Input.mousePosition.x, Input.mousePosition.y));
            activeSource = InputSource.None;
        }
    }

    private void PollTouches()
    {
        if (activeSource == InputSource.Mouse) return;
        if (Input.touchCount <= 0) return;

        for (int i = 0; i < Input.touchCount; i++)
        {
            Touch t = Input.GetTouch(i);
            if (t.phase == TouchPhase.Began && activeSource == InputSource.None)
            {
                activeSource = InputSource.Touch;
                activeTouchFingerId = t.fingerId;
                downPos = t.position;
                downTimeMs = NowMs();
                continue;
            }
            if (activeSource != InputSource.Touch || t.fingerId != activeTouchFingerId) continue;
            if (t.phase == TouchPhase.Ended || t.phase == TouchPhase.Canceled)
            {
                ProcessUp(t.position);
                activeSource = InputSource.None;
                activeTouchFingerId = -1;
            }
        }
    }

    /// <summary>
    /// 检测 EventSystem.current.currentSelectedGameObject 的变化，
    /// 当选中从 InputField/TMP_InputField 切走时触发 input_text 事件。
    /// </summary>
    private void TrackInputFieldSelectionChange()
    {
        EventSystem es = EventSystem.current;
        GameObject cur = es != null ? es.currentSelectedGameObject : null;
        if (cur == lastSelectedGo) return;

        if (lastSelectedGo != null)
        {
            EmitPendingEditBoxInput(lastSelectedGo);
        }
        lastSelectedGo = cur;
    }

    // ======================== click / swipe 处理 ========================

    private void ProcessUp(Vector2 upPos)
    {
        if (!downPos.HasValue) return;

        Vector2 down = downPos.Value;
        Vector2 delta = upPos - down;
        float distance = delta.magnitude;
        double duration = (NowMs() - downTimeMs) / 1000.0;
        float[] startNorm = ScreenToNorm(down);
        float[] endNorm = ScreenToNorm(upPos);
        long tsMs = downTimeMs - recordingStartTimeMs;

        downPos = null;

        if (distance > SWIPE_THRESHOLD_PX)
        {
            EmitSwipe(startNorm, endNorm, duration, tsMs);
            return;
        }
        EmitClick(startNorm, tsMs, duration);
    }

    private void EmitSwipe(float[] startNorm, float[] endNorm, double duration, long tsMs)
    {
        List<HitNodeInfo> hitNodes = CollectHitNodeInfos(startNorm[0], startNorm[1]);
        SendRecordEvent(new RecordEvent
        {
            action = "swipe",
            position = startNorm,
            end_position = endNorm,
            hit_nodes = hitNodes,
            duration = Math.Round(duration, 3),
            timestamp_ms = tsMs,
        });
    }

    private void EmitClick(float[] startNorm, long tsMs, double duration)
    {
        float[] clickNorm = new float[]
        {
            (float)Math.Round(startNorm[0], 4),
            (float)Math.Round(startNorm[1], 4),
        };
        List<HitNodeInfo> hitNodeInfos = CollectHitNodeInfos(startNorm[0], startNorm[1]);

        SendRecordEvent(new RecordEvent
        {
            action = "click",
            position = clickNorm,
            hit_nodes = hitNodeInfos,
            duration = Math.Round(duration, 3),
            timestamp_ms = tsMs,
        });

        if (HasInputFieldNode(hitNodeInfos))
        {
            pendingEditBoxHitNodes = FilterInputFieldNodes(hitNodeInfos);
            pendingClickPosition = clickNorm;
            return;
        }
        pendingEditBoxHitNodes = null;
        pendingClickPosition = null;
    }

    private static bool HasInputFieldNode(List<HitNodeInfo> hits)
    {
        if (hits == null) return false;
        for (int i = 0; i < hits.Count; i++)
        {
            if (IsInputFieldComponents(hits[i].components)) return true;
        }
        return false;
    }

    private static List<HitNodeInfo> FilterInputFieldNodes(List<HitNodeInfo> hits)
    {
        List<HitNodeInfo> result = new List<HitNodeInfo>();
        if (hits == null) return result;
        for (int i = 0; i < hits.Count; i++)
        {
            if (IsInputFieldComponents(hits[i].components)) result.Add(hits[i]);
        }
        return result;
    }

    private static bool IsInputFieldComponents(List<string> components)
    {
        if (components == null) return false;
        for (int i = 0; i < components.Count; i++)
        {
            string c = components[i];
            if (c == "InputField" || c == "TMP_InputField") return true;
        }
        return false;
    }

    private void EmitPendingEditBoxInput(GameObject prevSelected)
    {
        if (prevSelected == null) return;
        if (pendingEditBoxHitNodes == null || pendingEditBoxHitNodes.Count == 0) return;

        string text = ReadInputFieldText(prevSelected);
        long tsMs = NowMs() - recordingStartTimeMs;

        SendRecordEvent(new RecordEvent
        {
            action = "input_text",
            position = pendingClickPosition ?? new float[] { 0.5f, 0.5f },
            hit_nodes = pendingEditBoxHitNodes,
            text = text,
            timestamp_ms = tsMs,
        });
        pendingEditBoxHitNodes = null;
        pendingClickPosition = null;
    }

    private static string ReadInputFieldText(GameObject go)
    {
        if (go == null) return "";
        TMP_InputField tmpInput = go.GetComponent<TMP_InputField>();
        if (tmpInput != null) return tmpInput.text ?? "";
        InputField inp = go.GetComponent<InputField>();
        if (inp != null) return inp.text ?? "";
        return "";
    }

    // ======================== 命中检测 ========================

    private List<HitNodeInfo> CollectHitNodeInfos(float normX, float normY)
    {
        List<HitNodeInfo> all = new List<HitNodeInfo>();
        for (int i = 0; i < cameraConfigList.Count; i++)
        {
            CameraConfigEntry entry = cameraConfigList[i];
            if (entry.CameraType == "2d")
            {
                List<HitNodeInfo> hits = CollectUIHitsForEntry(entry, normX, normY);
                if (hits != null) all.AddRange(hits);
            }
            else
            {
                List<HitNodeInfo> hits = Collect3DHitsForEntry(entry, normX, normY);
                if (hits != null) all.AddRange(hits);
            }
        }
        return all;
    }

    /// <summary>
    /// 2D UI 命中：用 EventSystem.RaycastAll 取所有命中 UI，
    /// 再过滤出位于 entry.PathNode 子树下的节点。
    /// </summary>
    private List<HitNodeInfo> CollectUIHitsForEntry(CameraConfigEntry entry, float normX, float normY)
    {
        List<HitNodeInfo> result = new List<HitNodeInfo>();

        Camera cam = ResolveEntryCamera(entry);
        if (cam == null) return result;

        Transform rootNode = string.IsNullOrEmpty(entry.PathNode) ? null : Locate.FindTransformByPath(entry.PathNode);

        EventSystem es = EventSystem.current;
        if (es == null) return result;

        Vector2 screenPos = NormToScreen(normX, normY);
        PointerEventData ped = new PointerEventData(es) { position = screenPos };
        List<RaycastResult> raycasts = new List<RaycastResult>();
        es.RaycastAll(ped, raycasts);

        HashSet<int> seen = new HashSet<int>();
        int order = 0;
        for (int i = 0; i < raycasts.Count; i++)
        {
            GameObject go = raycasts[i].gameObject;
            if (go == null || !go.activeInHierarchy) continue;

            Transform t = go.transform;
            if (rootNode != null && !IsDescendantOf(t, rootNode)) continue;

            int id = go.GetInstanceID();
            if (seen.Contains(id)) continue;
            seen.Add(id);

            result.Add(BuildHitNodeInfo(t, cam, order, entry.PathCamera, false));
            order++;
        }
        return result;
    }

    /// <summary>
    /// 3D 物理命中：Camera.ScreenPointToRay + Physics.RaycastAll，
    /// 同样按 entry.PathNode 子树过滤。
    /// </summary>
    private List<HitNodeInfo> Collect3DHitsForEntry(CameraConfigEntry entry, float normX, float normY)
    {
        List<HitNodeInfo> result = new List<HitNodeInfo>();

        Camera cam = ResolveEntryCamera(entry);
        if (cam == null) return result;

        Transform rootNode = string.IsNullOrEmpty(entry.PathNode) ? null : Locate.FindTransformByPath(entry.PathNode);

        Vector2 screenPos = NormToScreen(normX, normY);
        Ray ray = cam.ScreenPointToRay(new Vector3(screenPos.x, screenPos.y, 0f));
        RaycastHit[] hits;
        try
        {
            hits = Physics.RaycastAll(ray, Mathf.Infinity);
        }
        catch (Exception e)
        {
            Debug.LogWarning("[TouchRecorder] 3D raycast failed: " + e.Message);
            return result;
        }
        if (hits == null || hits.Length == 0) return result;

        HashSet<int> seen = new HashSet<int>();
        for (int i = 0; i < hits.Length; i++)
        {
            Collider col = hits[i].collider;
            if (col == null) continue;
            Transform target = col.transform.parent != null ? col.transform.parent : col.transform;
            if (!target.gameObject.activeInHierarchy) continue;
            if (rootNode != null && !IsDescendantOf(target, rootNode)) continue;

            int id = target.gameObject.GetInstanceID();
            if (seen.Contains(id)) continue;
            seen.Add(id);

            result.Add(BuildHitNodeInfo(target, cam, 0, entry.PathCamera, true));
        }
        return result;
    }

    private Camera ResolveEntryCamera(CameraConfigEntry entry)
    {
        if (entry == null || string.IsNullOrEmpty(entry.PathCamera)) return null;
        GameObject go = GameObject.Find(entry.PathCamera);
        if (go == null)
        {
            WarnOnce3D("[TouchRecorder] camera node not found: " + entry.PathCamera);
            return null;
        }
        Camera cam = go.GetComponent<Camera>();
        if (cam == null)
        {
            WarnOnce3D("[TouchRecorder] no Camera component on: " + entry.PathCamera);
            return null;
        }
        _cam3DWarnLogged = false;
        return cam;
    }

    private void WarnOnce3D(string msg)
    {
        if (_cam3DWarnLogged) return;
        Debug.LogWarning(msg);
        _cam3DWarnLogged = true;
    }

    private static bool IsDescendantOf(Transform node, Transform ancestor)
    {
        Transform cur = node;
        while (cur != null)
        {
            if (cur == ancestor) return true;
            cur = cur.parent;
        }
        return false;
    }

    // ======================== HitNodeInfo 构建 ========================

    private HitNodeInfo BuildHitNodeInfo(Transform t, Camera cam, int renderOrder, string locatorCamera, bool is3d)
    {
        GameObject go = t.gameObject;
        return new HitNodeInfo
        {
            path = ResolvePath(t),
            name = go.name,
            components = GetComponentNames(go),
            depth = ComputeDepth(t),
            area = is3d ? 0f : ComputeArea(t),
            interactable = ResolveInteractable(go),
            position = GetNodeNormPosition(t, cam),
            size = is3d ? new float[] { 0f, 0f } : GetNodeNormSize(t, cam),
            render_order = renderOrder,
            parent_chain = GetParentChain(t, 3, cam),
            is_3d = is3d ? (bool?)true : null,
            locator_camera = locatorCamera,
        };
    }

    /// <summary>
    /// 优先取节点上挂载的 LocatorPath.locatorPath；但会验证该路径是否与当前
    /// 运行时层级一致（防止 Dropdown 克隆等情况导致 LocatorPath 过期）。
    /// 不一致时退化到带索引的 hierarchy 路径。
    /// </summary>
    private static string ResolvePath(Transform t)
    {
        LocatorPath lp = t.GetComponent<LocatorPath>();
        if (lp != null && !string.IsNullOrEmpty(lp.locatorPath))
        {
            if (IsLocatorPathValid(t, lp.locatorPath))
            {
                return lp.locatorPath;
            }
        }
        return GetIndexedPath(t);
    }

    /// <summary>
    /// 从叶到根逐级比较 transform.name 与 locatorPath 中的各段。
    /// 任何一级名称不匹配即返回 false（说明 LocatorPath 是过期的，
    /// 例如 TMP_Dropdown 在运行时把 Template 克隆为 Dropdown List 并重命名 Item）。
    /// </summary>
    private static bool IsLocatorPathValid(Transform t, string locatorPath)
    {
        string[] segments = locatorPath.Split('/');
        Transform cur = t;
        for (int i = segments.Length - 1; i >= 0; i--)
        {
            if (cur == null) return false;
            if (cur.name != segments[i]) return false;
            cur = cur.parent;
        }
        return true;
    }

    /// <summary>
    /// 模仿 Cocos 的 getIndexedPath：遇到同名兄弟时附加 [index]。
    /// </summary>
    private static string GetIndexedPath(Transform t)
    {
        List<string> segments = new List<string>();
        Transform cur = t;
        while (cur != null && cur.parent != null)
        {
            Transform parent = cur.parent;
            string seg = cur.name;

            int sameCount = 0;
            int myIndex = 0;
            for (int i = 0; i < parent.childCount; i++)
            {
                Transform sibling = parent.GetChild(i);
                if (sibling.name != cur.name) continue;
                if (sibling != cur && !sibling.gameObject.activeInHierarchy) continue;
                if (sibling == cur) myIndex = sameCount;
                sameCount++;
            }
            if (sameCount > 1) seg += "[" + myIndex + "]";
            segments.Insert(0, seg);
            cur = parent;
        }
        if (cur != null) segments.Insert(0, cur.name);
        return string.Join("/", segments.ToArray());
    }

    private static int ComputeDepth(Transform t)
    {
        int depth = 0;
        Transform cur = t.parent;
        while (cur != null) { depth++; cur = cur.parent; }
        return depth;
    }

    private static float ComputeArea(Transform t)
    {
        RectTransform rt = t as RectTransform ?? t.GetComponent<RectTransform>();
        if (rt == null) return 0f;
        Vector2 sz = rt.rect.size;
        return Mathf.Abs(sz.x * sz.y);
    }

    private static bool? ResolveInteractable(GameObject go)
    {
        Selectable sel = go.GetComponent<Selectable>();
        if (sel != null) return sel.interactable;
        return null;
    }

    private static List<string> GetComponentNames(GameObject go)
    {
        List<string> names = new List<string>();
        Component[] comps = go.GetComponents<Component>();
        for (int i = 0; i < comps.Length; i++)
        {
            Component c = comps[i];
            if (c == null) continue;
            names.Add(c.GetType().Name);
        }
        return names;
    }

    private static List<ParentChainEntry> GetParentChain(Transform t, int maxUp, Camera cam)
    {
        List<ParentChainEntry> chain = new List<ParentChainEntry>();
        Transform cur = t;
        for (int i = 0; i < maxUp; i++)
        {
            if (cur == null || cur.parent == null) break;
            cur = cur.parent;
            chain.Add(new ParentChainEntry
            {
                name = cur.name,
                path = ResolvePath(cur),
                components = GetComponentNames(cur.gameObject),
                position = GetNodeNormPosition(cur, cam),
                size = GetNodeNormSize(cur, cam),
            });
        }
        return chain;
    }

    // ======================== 坐标工具 ========================

    private static long NowMs()
    {
        return DateTimeOffset.UtcNow.ToUnixTimeMilliseconds();
    }

    /// <summary>
    /// Unity 屏幕坐标 (y 向上) → Cocos 风格归一化坐标 (y 向下，[0,1])。
    /// </summary>
    private static float[] ScreenToNorm(Vector2 screenPx)
    {
        float w = Screen.width <= 0 ? 1 : Screen.width;
        float h = Screen.height <= 0 ? 1 : Screen.height;
        float nx = screenPx.x / w;
        float ny = 1f - screenPx.y / h;
        return new float[] { nx, ny };
    }

    private static Vector2 NormToScreen(float normX, float normY)
    {
        float w = Screen.width <= 0 ? 1 : Screen.width;
        float h = Screen.height <= 0 ? 1 : Screen.height;
        return new Vector2(normX * w, (1f - normY) * h);
    }

    private static float[] GetNodeNormPosition(Transform t, Camera cam)
    {
        Vector2 sp = Locate.TransformToScreenPoint(t, cam);
        float w = Screen.width <= 0 ? 1 : Screen.width;
        float h = Screen.height <= 0 ? 1 : Screen.height;
        return new float[]
        {
            (float)Math.Round(sp.x / w, 4),
            (float)Math.Round(1f - sp.y / h, 4),
        };
    }

    private static float[] GetNodeNormSize(Transform t, Camera cam)
    {
        RectTransform rt = t as RectTransform ?? t.GetComponent<RectTransform>();
        if (rt == null) return new float[] { 0f, 0f };

        Vector3[] corners = new Vector3[4];
        rt.GetWorldCorners(corners);
        Vector3 minScreen = cam.WorldToScreenPoint(corners[0]);
        Vector3 maxScreen = cam.WorldToScreenPoint(corners[2]);

        float w = Screen.width <= 0 ? 1 : Screen.width;
        float h = Screen.height <= 0 ? 1 : Screen.height;
        return new float[]
        {
            (float)Math.Round(Math.Abs(maxScreen.x - minScreen.x) / w, 4),
            (float)Math.Round(Math.Abs(maxScreen.y - minScreen.y) / h, 4),
        };
    }

    // ======================== 推送 ========================

    private void SendRecordEvent(RecordEvent evt)
    {
        if (sendFn == null) return;
        sendFn(new { type = "record_event", data = evt });
    }
}
