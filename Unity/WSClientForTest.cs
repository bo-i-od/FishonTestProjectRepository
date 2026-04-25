using System;
using System.Collections;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
using UnityEngine.EventSystems;
using UnityEngine.SceneManagement;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

#if !UNITY_WEBGL || UNITY_EDITOR
using System.Net.WebSockets;
#endif

public class WSClientForTest : MonoBehaviour
{
#if UNITY_WEBGL && !UNITY_EDITOR
    [DllImport("__Internal")]
    private static extern int AutomationWS_Connect(string url);

    [DllImport("__Internal")]
    private static extern int AutomationWS_Send(string msg);

    [DllImport("__Internal")]
    private static extern void AutomationWS_Close();

    [DllImport("__Internal")]
    private static extern int AutomationWS_GetReadyState();
#else
    // ================== 编辑器原生 WebSocket 实现 ==================
    private static ClientWebSocket _editorWs;
    private static CancellationTokenSource _editorCts;
    private static readonly Queue<Action> _mainThreadActions = new Queue<Action>();

    private void AutomationWS_Connect(string url)
    {
        _editorWs = new ClientWebSocket();
        _editorCts = new CancellationTokenSource();
        Task.Run(() => ConnectEditorWs(url));
    }

    private async Task ConnectEditorWs(string url)
    {
        try
        {
            await _editorWs.ConnectAsync(new Uri(url), _editorCts.Token);
            _mainThreadActions.Enqueue(() => OnWsOpenFromPlugin(""));

            var buffer = new byte[8192];
            while (_editorWs.State == WebSocketState.Open)
            {
                var result = await _editorWs.ReceiveAsync(new ArraySegment<byte>(buffer), _editorCts.Token);
                if (result.MessageType == WebSocketMessageType.Close)
                {
                    await _editorWs.CloseAsync(WebSocketCloseStatus.NormalClosure, string.Empty, CancellationToken.None);
                    _mainThreadActions.Enqueue(() => OnWsCloseFromPlugin(""));
                }
                else
                {
                    string message = Encoding.UTF8.GetString(buffer, 0, result.Count);
                    _mainThreadActions.Enqueue(() => OnWsMessageFromPlugin(message));
                }
            }
        }
        catch (Exception ex)
        {
            Debug.LogWarning($"[Editor WS] Connection Error: {ex.Message}");
            _mainThreadActions.Enqueue(() => OnWsCloseFromPlugin(""));
        }
    }

    private void AutomationWS_Send(string msg)
    {
        if (_editorWs != null && _editorWs.State == WebSocketState.Open)
        {
            var bytes = Encoding.UTF8.GetBytes(msg);
            _editorWs.SendAsync(new ArraySegment<byte>(bytes), WebSocketMessageType.Text, true, _editorCts.Token);
        }
    }

    private void AutomationWS_Close()
    {
        if (_editorWs != null)
        {
            _editorCts?.Cancel();
            _editorWs.Dispose();
            _editorWs = null;
        }
    }
#endif

    [Header("WebSocket Settings")]
    public string ipAndPort = "127.0.0.1:5101";
    private int baseDelay = 500;
    private bool isReconnecting = false;
    private bool isConnected = false;

    private Dictionary<string, Func<JArray, object>> rpcHandlers = new Dictionary<string, Func<JArray, object>>();

    private static bool consoleTransmitted = false;
    private static int consoleTransmitLevel = 1; // 0=全部, 1=warn+error, 2=仅error
    private const float RefreshLocatorIntervalSeconds = 5f;

    private int[] screenSize => new int[] { Screen.width, Screen.height };

    private Camera TryGetCameraByPath(string path)
    {
        if (string.IsNullOrEmpty(path))
        {
            return null;
        }
        GameObject cameraObj = GameObject.Find(path);
        if (cameraObj == null)
        {
            return null;
        }
        return cameraObj.GetComponent<Camera>();
    }

    private Camera ResolveCamera(string locatorCamera)
    {
        if (string.IsNullOrEmpty(locatorCamera))
        {
            return null;
        }
        return TryGetCameraByPath(locatorCamera);
    }

    private Camera GetCamera(Dictionary<string, object> locator)
    {
        if (locator.TryGetValue("locator_camera", out object lc) && !string.IsNullOrEmpty(lc?.ToString()))
        {
            Camera c = ResolveCamera(lc.ToString());
            if (c != null) return c;
        }
        if (locator.TryGetValue("locator", out object loc) && !string.IsNullOrEmpty(loc?.ToString()))
        {
            string registryPath = CameraRegistry.FindCameraPathForNode(loc.ToString());
            if (!string.IsNullOrEmpty(registryPath))
            {
                Camera c = ResolveCamera(registryPath);
                if (c != null) return c;
            }
        }
        throw new Exception($"[WSClient] Camera Not Found! 请检查 locator_camera 或 CameraRegistry 注册项 (locator={JsonConvert.SerializeObject(locator)})");
    }

    private Camera GetCameraByLocator(string locatorCamera, string contextTag)
    {
        if (!string.IsNullOrEmpty(locatorCamera))
        {
            Camera c = ResolveCamera(locatorCamera);
            if (c != null) return c;
        }
        foreach (var entry in CameraRegistry.List())
        {
            if (entry.CameraType != "2d") continue;
            Camera c = ResolveCamera(entry.PathCamera);
            if (c != null) return c;
        }
        throw new Exception($"[{contextTag}] Camera Not Found. locator='{locatorCamera}'，CameraRegistry 中未注册可用的 2d 相机。");
    }

    void Start()
    {
        DontDestroyOnLoad(gameObject);

        RegisterAllRpcs();
        InvokeRepeating(nameof(RefreshLocator), 0f, RefreshLocatorIntervalSeconds);

        StartConnection();
        TransmitConsole();
    }

    void Update()
    {
#if !UNITY_WEBGL || UNITY_EDITOR
        while (_mainThreadActions.Count > 0)
        {
            var action = _mainThreadActions.Dequeue();
            action?.Invoke();
        }
#endif
    }

    #region 核心注册与执行

    private void RegisterAllRpcs()
    {
        RegisterRpcHandler("GetScreenSize", GetScreenSize);
        RegisterRpcHandler("CMD", CMD);
        RegisterRpcHandler("Screenshot", Screenshot);
        RegisterRpcHandler("SetText", SetText);
        RegisterRpcHandler("SetTextById", SetTextById);
        RegisterRpcHandler("GetText", GetText);
        RegisterRpcHandler("GetTextById", GetTextById);
        RegisterRpcHandler("GetSliderValue", GetSliderValue);
        RegisterRpcHandler("GetSliderValueById", GetSliderValueById);
        RegisterRpcHandler("GetImgName", GetImgName);
        RegisterRpcHandler("GetImgNameById", GetImgNameById);
        RegisterRpcHandler("GetName", GetName);
        RegisterRpcHandler("GetNameById", GetNameById);
        RegisterRpcHandler("GetPosition", GetPosition);
        RegisterRpcHandler("GetPositionById", GetPositionById);
        RegisterRpcHandler("GetSize", GetSize);
        RegisterRpcHandler("GetSizeById", GetSizeById);
        RegisterRpcHandler("GetObjectId", GetObjectId);
        RegisterRpcHandler("GetOffspringIdById", GetOffspringIdById);
        RegisterRpcHandler("GetParentId", GetParentId);
        RegisterRpcHandler("GetParentIdById", GetParentIdById);
        RegisterRpcHandler("GetToggleIsOn", GetToggleIsOn);
        RegisterRpcHandler("GetToggleIsOnById", GetToggleIsOnById);
        RegisterRpcHandler("SetBtnEnabled", SetBtnEnabled);
        RegisterRpcHandler("SetObjectActive", SetObjectActive);
        RegisterRpcHandler("SetDropdownValue", SetDropdownValue);
        RegisterRpcHandler("GetDropdownValue", GetDropdownValue);
        RegisterRpcHandler("ClickButton", ClickButton);
        RegisterRpcHandler("RayInput", RayInput);
        RegisterRpcHandler("RayInputById", RayInputById);
        RegisterRpcHandler("CustomCMD", CustomCMD);
        RegisterRpcHandler("SetCamera", SetCameraRpc);
        RegisterRpcHandler("RemoveCamera", RemoveCameraRpc);
        RegisterRpcHandler("SetTimeScale", SetTimeScale);
        RegisterRpcHandler("SetSendLogFlag", SetSendLogFlag);
    }

    public void GetLocatorPathComponent(GameObject gameObject, string path)
    {
        if (!gameObject.TryGetComponent(out LocatorPath locatorPath))
        {
            locatorPath = gameObject.AddComponent<LocatorPath>();
        }
        locatorPath.AddWSClientForTestManager(this.gameObject);
        locatorPath.RefreshLocatorPath(path);
    }
    private void RefreshLocator()
    {
        int totalCount = 0;

        // 遍历所有已加载的场景（包括 Additive 加载的场景）
        for (int i = 0; i < SceneManager.sceneCount; i++)
        {
            Scene scene = SceneManager.GetSceneAt(i);
            if (!scene.isLoaded) continue;

            GameObject[] rootGameObjects = scene.GetRootGameObjects();
            totalCount += rootGameObjects.Length;
            foreach (GameObject rootObj in rootGameObjects)
            {
                GetLocatorPathComponent(rootObj, "");
            }
        }

        // 获取 DontDestroyOnLoad 场景中的根节点
        GameObject ddolProbe = new GameObject("__DDOLProbe__");
        DontDestroyOnLoad(ddolProbe);
        Scene ddolScene = ddolProbe.scene;
        Destroy(ddolProbe);

        GameObject[] ddolRoots = ddolScene.GetRootGameObjects();
        totalCount += ddolRoots.Length;
        foreach (GameObject rootObj in ddolRoots)
        {
            if (rootObj.name == "__DDOLProbe__") continue;
            GetLocatorPathComponent(rootObj, "");
        }
    }

    public void RegisterRpcHandler(string methodName, Func<JArray, object> callback)
    {
        if (string.IsNullOrEmpty(methodName) || callback == null) return;
        rpcHandlers[methodName] = callback;
    }

    private void StartConnection()
    {
        if (string.IsNullOrEmpty(ipAndPort)) return;
        string url = $"ws://{ipAndPort}";
        Debug.Log($"[WSClientForTest] Connecting to {url}...");
        AutomationWS_Connect(url);
    }

    private void HandleReconnect()
    {
        if (isReconnecting) return;
        isReconnecting = true;
        isConnected = false;
        StartCoroutine(ReconnectRoutine());
    }

    private IEnumerator ReconnectRoutine()
    {
        yield return new WaitForSeconds(baseDelay / 1000f);
        isReconnecting = false;
        StartConnection();
    }

    #endregion

    #region WebGL Plugin Callbacks

    public void OnWsOpenFromPlugin(string empty)
    {
        isConnected = true;
        Debug.Log("[WSClientForTest] WebSocket Connected!");
    }

    public void OnWsCloseFromPlugin(string empty)
    {
        Debug.LogWarning("[WSClientForTest] WebSocket Disconnected.");
        HandleReconnect();
    }

    public async void OnWsMessageFromPlugin(string jsonMessage)
    {
        if (string.IsNullOrEmpty(jsonMessage)) return;

        string response;
        string tempId = null;

        try
        {
            var data = JObject.Parse(jsonMessage);
            tempId = data["id"]?.ToString();
            string method = data["method"]?.ToString();

            if (string.IsNullOrEmpty(method)) return;

            if (!rpcHandlers.ContainsKey(method))
            {
                response = FormatResponseError(tempId, $"Method '{method}' not found");
                SendMsgToServer(response);
                return;
            }

            JArray paramsArray = data["params"] as JArray ?? new JArray();
            object result = rpcHandlers[method].Invoke(paramsArray);

            if (result is System.Threading.Tasks.Task task)
            {
                await task;
                var resultProp = task.GetType().GetProperty("Result");
                result = resultProp != null ? resultProp.GetValue(task) : null;
            }

            response = FormatResponse(tempId, result);
            SendMsgToServer(response);
        }
        catch (Exception ex)
        {
            Debug.LogError($"[WSClientForTest] Critical Error: {ex.Message}");
            response = FormatResponseError(tempId, ex.Message);
            SendMsgToServer(response);
        }
    }

    private void SendMsgToServer(string msg)
    {
        if (!isConnected || string.IsNullOrEmpty(msg)) return;
        AutomationWS_Send(msg);
    }

    #endregion

    #region 消息格式化 & 日志

    private string FormatMessage(string idAction, object msg)
    {
        return JsonConvert.SerializeObject(new { jsonrpc = "2.0", id = idAction, msg = msg });
    }

    private string FormatResponse(string idAction, object res)
    {
        return JsonConvert.SerializeObject(new { jsonrpc = "2.0", id = idAction, result = res });
    }

    private string FormatResponseError(string idAction, string errMsg)
    {
        return JsonConvert.SerializeObject(new { jsonrpc = "2.0", id = idAction, error = new { code = -32000, message = errMsg } });
    }

    private void TransmitConsole()
    {
        if (consoleTransmitted) return;
        consoleTransmitted = true;
        Application.logMessageReceived += HandleUnityLog;
    }

    private void HandleUnityLog(string logString, string stackTrace, LogType type)
    {
        if (!isConnected) return;
        int msgLevel = 0;
        string logTypeStr = "log";

        switch (type)
        {
            case LogType.Log: msgLevel = 0; logTypeStr = "log"; break;
            case LogType.Warning: msgLevel = 1; logTypeStr = "warn"; break;
            case LogType.Error: case LogType.Exception: case LogType.Assert: msgLevel = 2; logTypeStr = "error"; break;
        }

        if (msgLevel < consoleTransmitLevel) return;

        try
        {
            var msgObj = new { type = logTypeStr, data = logString };
            string msg = FormatMessage("", msgObj);
            SendMsgToServer(msg);
        }
        catch { }
    }

    void OnDestroy()
    {
        CancelInvoke(nameof(RefreshLocator));
        Application.logMessageReceived -= HandleUnityLog;
        consoleTransmitted = false;
        AutomationWS_Close();
    }
    #endregion

    #region 移植的 RPC 业务方法

    private object GetScreenSize(JArray paramArray)
    {
        return new[] { Screen.width, Screen.height };
    }

    private object CMD(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        JArray jArray = (JArray)param[0];
        List<string> cmdList = jArray.ToObject<List<string>>();
        for (int cur = 0; cur < cmdList.Count; cur++)
        {
            Cmd(cmdList[cur]);
        }
        return null;
    }

    public void Cmd(string cmd)
    {
        // 占位
    }

    private object CustomCMD(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        JArray jArray = (JArray)param[0];
        List<string> cmdList = jArray.ToObject<List<string>>();
        for (int cur = 0; cur < cmdList.Count; cur++)
        {
            CustomCMD(cmdList[cur]);
        }
        return null;
    }

    private void CustomCMD(string cmd)
    {
        // camera config is now handled by SetCamera/RemoveCamera RPC via CameraRegistry
    }

    private object SetCameraRpc(JArray paramArray)
    {
        string pathNode = paramArray[0].ToString();
        string pathCamera = paramArray[1].ToString();
        string cameraType = paramArray[2].ToString();
        CameraRegistry.Set(pathNode, pathCamera, cameraType);
        return true;
    }

    private object RemoveCameraRpc(JArray paramArray)
    {
        string pathNode = paramArray[0].ToString();
        CameraRegistry.Remove(pathNode);
        return true;
    }

    private object Screenshot(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        int x = Convert.ToInt32(param[0]);
        int y = Convert.ToInt32(param[1]);
        int width = Convert.ToInt32(param[2]);
        int height = Convert.ToInt32(param[3]);
        Camera uiCamer = GetCameraByLocator("", "Screenshot");
        RenderTexture rt = new RenderTexture((int)screenSize[0], (int)screenSize[1], 0);
        uiCamer.targetTexture = rt;
        uiCamer.Render();
        RenderTexture.active = rt;
        var tex = new Texture2D(width, height, TextureFormat.RGB24, false);
        tex.ReadPixels(new Rect(x - 0.5f * width, y - 0.5f * height, width, height), 0, 0);
        tex.Apply(false);
        byte[] fileBytes = tex.EncodeToJPG(80);
        string b64img = Convert.ToBase64String(fileBytes);
        uiCamer.targetTexture = null;
        RenderTexture.active = null;
        Destroy(rt);
        return new object[] { b64img, "jpg" };
    }

    private object GetText(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        List<List<string>> res = new List<List<string>>();
        for (int cur = 0; cur < locatorList.Count; cur++)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            res.Add(Locate.GetTextList(targetList));
        }
        return res;
    }

    private object SetText(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        for (int cur = 0; cur < locatorList.Count; cur++)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            Locate.SetTextList(targetList, param[1].ToString());
        }
        return null;
    }

    private object GetSliderValue(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        List<List<float>> res = new List<List<float>>();
        for (int cur = 0; cur < locatorList.Count; cur++)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            res.Add(Locate.GetSliderValueList(targetList));
        }
        return res;
    }

    private object GetDropdownValue(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        List<List<int>> res = new List<List<int>>();
        for (int cur = 0; cur < locatorList.Count; cur++)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            List<int> tempRes = new List<int>();
            for (int i = 0; i < targetList.Count; i++)
            {
                tempRes.Add(targetList[i].GetComponent<TMP_Dropdown>().value);
            }
            res.Add(tempRes);
        }
        return res;
    }

    private object SetDropdownValue(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        for (int cur = 0; cur < locatorList.Count; cur++)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            for (int i = 0; i < targetList.Count; i++)
            {
                targetList[i].GetComponent<TMP_Dropdown>().value = Convert.ToInt32(param[1]);
            }
        }
        return null;
    }

    private object GetName(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        List<List<string>> res = new List<List<string>>();
        for (int cur = 0; cur < locatorList.Count; cur++)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            res.Add(Locate.GetNameList(targetList));
        }
        return res;
    }

    private object GetImgName(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        List<List<string>> res = new List<List<string>>();
        for (int cur = 0; cur < locatorList.Count; cur++)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            res.Add(Locate.GetImgNameList(targetList));
        }
        return res;
    }

    public object GetPosition(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        List<List<float[]>> res = new List<List<float[]>>();
        for (int cur = 0; cur < locatorList.Count; cur++)
        {
            Dictionary<string, object> locator = locatorList[cur];
            Camera uiCamer = GetCamera(locator);

            float[] focus = { 0.5f, 0.5f };
            if (locator.ContainsKey("focus"))
            {
                JArray jArray = (JArray)locator["focus"];
                focus = jArray.ToObject<float[]>();
            }
            List<Transform> targetList = Locate.LocateTransform(locator);
            List<float[]> position = Locate.GetPositionList(targetList, screenSize, uiCamer);
            List<float[]> size = Locate.GetSizeList(targetList);
            res.Add(Locate.CorrectPosition(position, size, focus));
        }
        return res;
    }

    public object GetSize(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        List<List<float[]>> res = new List<List<float[]>>();
        for (int cur = 0; cur < locatorList.Count; cur++)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            res.Add(Locate.GetSizeList(targetList));
        }
        return res;
    }

    private object GetTextById(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        List<List<string>> res = new List<List<string>>();
        JArray jArray = (JArray)param[0];
        List<int> instanceIdList = jArray.ToObject<List<int>>();
        string offspringPath = param[1].ToString();
        for (int cur = 0; cur < instanceIdList.Count; cur++)
        {
            int instanceId = instanceIdList[cur];
            List<Transform> transformList = Locate.GetTransformListByInstanceID(instanceId, offspringPath);
            res.Add(Locate.GetTextList(transformList));
        }
        return res;
    }

    private object SetTextById(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        JArray jArray = (JArray)param[0];
        List<int> instanceIdList = jArray.ToObject<List<int>>();
        string offspringPath = param[1].ToString();
        string textVal = param[2].ToString();
        for (int cur = 0; cur < instanceIdList.Count; cur++)
        {
            int instanceId = instanceIdList[cur];
            List<Transform> transformList = Locate.GetTransformListByInstanceID(instanceId, offspringPath);
            Locate.SetTextList(transformList, textVal);
        }
        return null;
    }

    private object GetSliderValueById(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        List<List<float>> res = new List<List<float>>();
        JArray jArray = (JArray)param[0];
        List<int> instanceIdList = jArray.ToObject<List<int>>();
        string offspringPath = param[1].ToString();
        for (int cur = 0; cur < instanceIdList.Count; cur++)
        {
            int instanceId = instanceIdList[cur];
            List<Transform> transformList = Locate.GetTransformListByInstanceID(instanceId, offspringPath);
            res.Add(Locate.GetSliderValueList(transformList));
        }
        return res;
    }

    private object GetNameById(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        List<List<string>> res = new List<List<string>>();
        JArray jArray = (JArray)param[0];
        List<int> instanceIdList = jArray.ToObject<List<int>>();
        string offspringPath = param[1].ToString();
        for (int cur = 0; cur < instanceIdList.Count; cur++)
        {
            int instanceId = instanceIdList[cur];
            List<Transform> transformList = Locate.GetTransformListByInstanceID(instanceId, offspringPath);
            res.Add(Locate.GetNameList(transformList));
        }
        return res;
    }

    private object GetImgNameById(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        List<List<string>> res = new List<List<string>>();
        JArray jArray = (JArray)param[0];
        List<int> instanceIdList = jArray.ToObject<List<int>>();
        string offspringPath = param[1].ToString();
        for (int cur = 0; cur < instanceIdList.Count; cur++)
        {
            int instanceId = instanceIdList[cur];
            List<Transform> transformList = Locate.GetTransformListByInstanceID(instanceId, offspringPath);
            res.Add(Locate.GetImgNameList(transformList));
        }
        return res;
    }

    public object GetPositionById(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        List<List<float[]>> res = new List<List<float[]>>();
        JArray jArray = (JArray)param[0];
        List<int> instanceIdList = jArray.ToObject<List<int>>();
        string offspringPath = param[1].ToString();
        string cameraLocator = param[2].ToString();

        Camera uiCamer = GetCameraByLocator(cameraLocator, "GetPositionById");
        for (int cur = 0; cur < instanceIdList.Count; cur++)
        {
            int instanceId = instanceIdList[cur];
            List<Transform> transformList = Locate.GetTransformListByInstanceID(instanceId, offspringPath);
            res.Add(Locate.GetPositionList(transformList, screenSize, uiCamer));
        }
        return res;
    }

    public object GetSizeById(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        List<List<float[]>> res = new List<List<float[]>>();
        JArray jArray = (JArray)param[0];
        List<int> instanceIdList = jArray.ToObject<List<int>>();
        string offspringPath = param[1].ToString();
        for (int cur = 0; cur < instanceIdList.Count; cur++)
        {
            int instanceId = instanceIdList[cur];
            List<Transform> transformList = Locate.GetTransformListByInstanceID(instanceId, offspringPath);
            res.Add(Locate.GetSizeList(transformList));
        }
        return res;
    }

    public object GetObjectId(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        List<List<int>> res = new List<List<int>>();
        for (int cur = 0; cur < locatorList.Count; cur++)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            res.Add(Locate.GetInstanceIDList(targetList));
        }
        return res;
    }

    public object GetOffspringIdById(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        List<List<int>> res = new List<List<int>>();
        JArray jArray = (JArray)param[0];
        List<int> instanceIdList = jArray.ToObject<List<int>>();
        string offspringPath = param[1].ToString();
        for (int cur = 0; cur < instanceIdList.Count; cur++)
        {
            int instanceId = instanceIdList[cur];
            List<Transform> transformList = Locate.GetTransformListByInstanceID(instanceId, offspringPath);
            res.Add(Locate.GetInstanceIDList(transformList));
        }
        return res;
    }

    public object GetParentIdById(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        List<List<int>> res = new List<List<int>>();
        JArray jArray = (JArray)param[0];
        List<int> instanceIdList = jArray.ToObject<List<int>>();
        string offspringPath = param[1].ToString();
        for (int cur = 0; cur < instanceIdList.Count; cur++)
        {
            int instanceId = instanceIdList[cur];
            List<Transform> transformList = Locate.GetTransformListByInstanceID(instanceId, offspringPath);
            List<Transform> parentList = Locate.GetParentTransformList(transformList);
            res.Add(Locate.GetInstanceIDList(parentList));
        }
        return res;
    }

    public object GetParentId(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        List<List<int>> res = new List<List<int>>();
        for (int cur = 0; cur < locatorList.Count; cur++)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            List<Transform> parentList = Locate.GetParentTransformList(targetList);
            res.Add(Locate.GetInstanceIDList(parentList));
        }
        return res;
    }

    private object GetToggleIsOn(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        List<List<bool>> res = new List<List<bool>>();
        for (int cur = 0; cur < locatorList.Count; cur++)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            res.Add(Locate.GetToggleIsOnList(targetList));
        }
        return res;
    }

    private object GetToggleIsOnById(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        List<List<bool>> res = new List<List<bool>>();
        JArray jArray = (JArray)param[0];
        List<int> instanceIdList = jArray.ToObject<List<int>>();
        string offspringPath = param[1].ToString();
        for (int cur = 0; cur < instanceIdList.Count; cur++)
        {
            int instanceId = instanceIdList[cur];
            List<Transform> transformList = Locate.GetTransformListByInstanceID(instanceId, offspringPath);
            res.Add(Locate.GetToggleIsOnList(transformList));
        }
        return res;
    }

    private object SetBtnEnabled(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        bool enabled = (bool)param[1];
        for (int cur = 0; cur < locatorList.Count; cur++)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            for (int i = 0; i < targetList.Count; i++)
            {
                SetBtnEnabled(targetList[i], enabled);
            }
        }
        return null;
    }

    private object SetObjectActive(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        JArray pathJArray = (JArray)param[0];
        List<string> pathList = pathJArray.ToObject<List<string>>();
        bool active = (bool)param[1];

        foreach (string path in pathList)
        {
            Transform target = Locate.FindTransformByPath(path);
            if (target == null) continue;
            
            target.gameObject.SetActive(active);
        }
        
        return null;
    }

    private void SetBtnEnabled(Transform transform, bool enabled)
    {
        transform.TryGetComponent(out Button button);
        if (button != null)
        {
            button.enabled = enabled;
        }
        if (transform.childCount == 0)
        {
            return;
        }
        for (int cur = 0; cur < transform.childCount; cur++)
        {
            Transform childTranform = transform.GetChild(cur);
            SetBtnEnabled(childTranform, enabled);
        }
    }

    private object ClickButton(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        for (int cur = 0; cur < locatorList.Count; cur++)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            for (int i = 0; i < targetList.Count; i++)
            {
                Button button = targetList[i].GetComponent<Button>();
                if (button != null)
                {
                    button.onClick.Invoke();
                }
            }
        }
        return null;
    }

    private object RayInput(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        Dictionary<string, object> locator = locatorList[0];

        Camera cam = GetCamera(locator);

        List<Transform> targetList = Locate.LocateTransform(locator);

        string kind = param[1].ToString();
        if (targetList.Count < 1)
        {
            return null;
        }

        Transform target = targetList[0];
        string targetName = target.name;
        Vector2 screenVec = Locate.TransformToScreenPoint(target, cam);

        if (locator.ContainsKey("focus"))
        {
            JArray focus = (JArray)locator["focus"];
            float focus_x = focus[0].Value<float>();
            float focus_y = focus[1].Value<float>();
            RectTransform rt = target.GetComponent<RectTransform>();
            if (rt != null)
            {
                Vector2 size = rt.sizeDelta;
                screenVec[0] = screenVec[0] + (0.5f - focus_x) * size[0];
                screenVec[1] = screenVec[1] + (focus_y - 0.5f) * size[1];
            }
        }

        Vector3 screenPoint = new Vector3(screenVec[0], screenVec[1], 0f);
        RayInput(screenPoint, targetName, kind);
        return null;
    }

    private object RayInputById(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        JArray jArray = (JArray)param[0];
        List<int> instanceIdList = jArray.ToObject<List<int>>();
        string offspringPath = param[1].ToString();
        string kind = param[2].ToString();
        string cameraLocator = (param.Count > 3) ? param[3].ToString() : "";
        Camera cam = GetCameraByLocator(cameraLocator, "RayInputById");

        for (int cur = 0; cur < instanceIdList.Count; cur++)
        {
            int instanceId = instanceIdList[cur];
            List<Transform> transformList = Locate.GetTransformListByInstanceID(instanceId, offspringPath);
            if (transformList.Count < 1)
            {
                continue;
            }
            Transform target = transformList[0];
            string targetName = target.name;
            Vector2 screenVec = Locate.TransformToScreenPoint(target, cam);
            Vector3 screenPoint = new Vector3(screenVec[0], screenVec[1], 0f);
            RayInput(screenPoint, targetName, kind);
        }
        return null;
    }

    private void RayInput(Vector3 screenPoint, string targetName, string kind)
    {
        // 创建一个PointerEventData来存储点击事件的数据
        PointerEventData pointerData = new PointerEventData(EventSystem.current);
        pointerData.position = screenPoint;

        // 创建一个list来存储点击结果
        List<RaycastResult> results = new List<RaycastResult>();

        // 使用EventSystem的RaycastAll方法来检测当前点击位置上的UI元素
        EventSystem.current.RaycastAll(pointerData, results);
        foreach (RaycastResult result in results)
        {
            if (result.gameObject.name != targetName)
            {
                continue;
            }
            if (kind == "up")
            {
                ExecuteEvents.Execute(result.gameObject, pointerData, ExecuteEvents.pointerUpHandler);
                return;
            }
            if (kind == "down")
            {
                ExecuteEvents.Execute(result.gameObject, pointerData, ExecuteEvents.pointerDownHandler);
                return;
            }
            if (kind == "click")
            {
                ExecuteEvents.Execute(result.gameObject, pointerData, ExecuteEvents.pointerClickHandler);
                return;
            }
        }
    }

    private object SetTimeScale(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        Time.timeScale = Convert.ToSingle(param[0]);
        return null;
    }

    private bool sendLogFlag = true;
    private object SetSendLogFlag(JArray paramArray)
    {
        List<object> param = paramArray.ToObject<List<object>>();
        sendLogFlag = (bool)param[0];
        // 此处你可以结合日志控制逻辑，如果 sendLogFlag == false，就不发送日志
        return null;
    }

    #endregion
}