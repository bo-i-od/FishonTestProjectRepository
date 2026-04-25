using System.Collections.Generic;

/// <summary>
/// 相机配置条目。
/// pathNode:   节点路径（该节点 + 子树共享此相机）
/// pathCamera: 相机节点路径（GameObject.Find 可定位）
/// cameraType: "2d" 或 "3d"
/// </summary>
public class CameraConfigEntry
{
    public string PathNode;
    public string PathCamera;
    public string CameraType;
}

/// <summary>
/// 全局相机注册表。
/// 以 PathNode 为唯一键，支持最长前缀匹配查找。
/// C# 端各模块（WSClientForTest / LocatorPath 等）共享此注册表。
/// </summary>
public static class CameraRegistry
{
    private static readonly List<CameraConfigEntry> entries = new List<CameraConfigEntry>();

    public static void Set(string pathNode, string pathCamera, string cameraType)
    {
        var existing = FindExisting(pathNode);
        if (existing != null)
        {
            existing.PathCamera = pathCamera;
            existing.CameraType = cameraType;
            return;
        }
        entries.Add(new CameraConfigEntry
        {
            PathNode = pathNode,
            PathCamera = pathCamera,
            CameraType = cameraType
        });
    }

    public static void Remove(string pathNode)
    {
        entries.RemoveAll(e => e.PathNode == pathNode);
    }

    public static List<CameraConfigEntry> List()
    {
        return new List<CameraConfigEntry>(entries);
    }

    public static void Clear()
    {
        entries.Clear();
    }

    /// <summary>
    /// 最长前缀匹配：查找 nodePath 所属子树对应的相机路径。
    /// 匹配规则：
    ///   - entry.PathNode == nodePath  精确命中
    ///   - nodePath 以 entry.PathNode + "/" 开头  子树命中
    /// 取匹配段数最多者（最长前缀）；无命中返回 ""。
    /// </summary>
    public static string FindCameraPathForNode(string nodePath)
    {
        CameraConfigEntry bestEntry = null;
        int bestDepth = -1;
        for (int i = 0; i < entries.Count; i++)
        {
            var entry = entries[i];
            if (!IsNodeUnderPath(nodePath, entry.PathNode)) continue;
            int depth = entry.PathNode.Split('/').Length;
            if (depth > bestDepth)
            {
                bestDepth = depth;
                bestEntry = entry;
            }
        }
        return bestEntry != null ? bestEntry.PathCamera : "";
    }

    private static CameraConfigEntry FindExisting(string pathNode)
    {
        for (int i = 0; i < entries.Count; i++)
        {
            if (entries[i].PathNode == pathNode)
            {
                return entries[i];
            }
        }
        return null;
    }

    private static bool IsNodeUnderPath(string nodePath, string parentPath)
    {
        if (nodePath == parentPath) return true;
        return nodePath.StartsWith(parentPath + "/");
    }
}
