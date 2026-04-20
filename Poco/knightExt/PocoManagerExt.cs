#if !WEIXINMINIGAME || UNITY_EDITOR
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
using System;
using Newtonsoft.Json.Linq;
using UnityEngine.EventSystems;
using UnityEngine.SceneManagement;
using System.Net.Sockets;
using Poco;
using System.Runtime.ConstrainedExecution;


//用于扩展rpc，比如一些Command
public partial class PocoManager : MonoBehaviour
{
    private void addExtRpcMethods()
    {
        rpc.addRpcMethod("GetKnightInfo", GetKnightInfo);
        rpc.addRpcMethod("CMD", CMD);
        rpc.addRpcMethod("Screenshot", Screenshot);
        rpc.addRpcMethod("SetText", SetText);
        rpc.addRpcMethod("SetTextById", SetTextById);
        rpc.addRpcMethod("GetText", GetText);
        rpc.addRpcMethod("GetTextById", GetTextById);
        rpc.addRpcMethod("GetSliderValue", GetSliderValue);
        rpc.addRpcMethod("GetSliderValueById", GetSliderValueById);
        rpc.addRpcMethod("GetImgName", GetImgName);
        rpc.addRpcMethod("GetImgNameById", GetImgNameById);
        rpc.addRpcMethod("GetName", GetName);
        rpc.addRpcMethod("GetNameById", GetNameById);
        rpc.addRpcMethod("GetPosition", GetPosition);
        rpc.addRpcMethod("GetPositionById", GetPositionById);
        rpc.addRpcMethod("GetSize", GetSize);
        rpc.addRpcMethod("GetSizeById", GetSizeById);
        rpc.addRpcMethod("GetObjectId", GetObjectId);
        rpc.addRpcMethod("GetOffspringIdById", GetOffspringIdById);
        rpc.addRpcMethod("GetParentId", GetParentId);
        rpc.addRpcMethod("GetParentIdById", GetParentIdById);
        rpc.addRpcMethod("GetToggleIsOn", GetToggleIsOn);
        rpc.addRpcMethod("GetToggleIsOnById", GetToggleIsOnById);
        rpc.addRpcMethod("SetBtnEnabled", SetBtnEnabled);
        rpc.addRpcMethod("SetObjectActive", SetObjectActive);
        rpc.addRpcMethod("SetObjectActiveById", SetObjectActiveById);
        rpc.addRpcMethod("SetDropdownValue", SetDropdownValue);
        rpc.addRpcMethod("GetDropdownValue", GetDropdownValue);
        rpc.addRpcMethod("ClickButton", ClickButton);
        rpc.addRpcMethod("RayInput", RayInput);
        rpc.addRpcMethod("RayInputById", RayInputById);
        rpc.addRpcMethod("CustomCMD", CustomCMD);
        rpc.addRpcMethod("SetTimeScale", SetTimeScale);
        rpc.addRpcMethod("SetSendLogFlag", SetSendLogFlag);
        rpc.addRpcMethod("RegisterPushChannel", RegisterPushChannel);
    }

    public void GetLocatorPathComponent(GameObject gameObject, string path)
    {
        if (!gameObject.TryGetComponent(out LocatorPath locatorPath))
        {
            locatorPath = gameObject.AddComponent<LocatorPath>();
        }
        locatorPath.AddPocoManager(this.gameObject);
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

    private bool AbleToSend()
    {
        if (!sendLogFlag)
        {
            return false;
        }
        if (clientSend == null)
        {
            return false;
        }
        // Poll方法用于检查底层Socket的状态。如果返回true，表示有数据可读或连接已断开。如果返回false，表示连接正常。
        if (clientSend.Client.Poll(0, SelectMode.SelectRead))
        {
            clientSend = null;
            return false;
        }
        return true;
    }

    public void CsToPython(string msg)
    {
        if (!AbleToSend())
        {
            return;
        }
        // ...你的业务逻辑...
        string response = rpc.formatMessage(msg, Guid.NewGuid().ToString("D"));
        // 通过tcpClient对象发送数据
        byte[] bytes = prot.pack(response);
        server.Send(clientSend, bytes);
    }

    public void CsToPython(string method, List<object> param = null)
    {
        if (!AbleToSend())
        {
            return;
        }
        // ...你的业务逻辑...
        string response = rpc.formatRequest(method, Guid.NewGuid().ToString("D"), param);
        // 通过tcpClient对象发送数据
        byte[] bytes = prot.pack(response);
        server.Send(clientSend, bytes);
    }

    [RPC]
    private object GetKnightInfo(List<object> param)
    {
        /* 对应到Python可能的调用样例
        def getKnightInfo(self)
            self.poco.agent.rpc.call("GetKnightInfo").wait()
            sleep(2)
        */
        return "v1.0";
    }

    [RPC]
    private object CMD(List<object> param)
    {
        JArray jArray = (JArray)param[0];
        List<string> cmdList = jArray.ToObject<List<string>>();
        int cur = 0;
        while (cur < cmdList.Count)
        {
            Cmd(cmdList[cur]);
            cur += 1;
        }
        return null;
    }

    public void Cmd(string cmd)
    {
        // GameEventManager.Instance.SendEvent(GameEventMsg.POCO_CMD, cmd);
        // 注释掉这行代码，因为GameEventManager和GameEventMsg在项目中不存在
    }

    [RPC]
    private object CustomCMD(List<object> param)
    {
        JArray jArray = (JArray)param[0];
        List<string> cmdList = jArray.ToObject<List<string>>();
        int cur = 0;
        while (cur < cmdList.Count)
        {
            CustomCMD(cmdList[cur]);
            cur += 1;
        }
        return null;
    }

    private void CustomCMD(string cmd)
    {
        string[] cmdArray = cmd.Split(' ');
        if (cmdArray[0] == "setCamera")
        {
            cameraNameDefault = cmd.Split(' ', 2)[1];
            return;
        }

    }


    // 输入 坐标和截图尺寸
    // 返回 base64格式的图像数据
    [RPC]
    private object Screenshot(List<object> param)
    {

        int x = Convert.ToInt32(param[0]);
        int y = Convert.ToInt32(param[1]);
        
        int width = Convert.ToInt32(param[2]);
        int height = Convert.ToInt32(param[3]);
        Camera uiCamer = GameObject.Find(cameraNameDefault).GetComponent<Camera>();
        RenderTexture rt = new RenderTexture(screenSize[0], screenSize[1], 0);
        uiCamer.targetTexture = rt;
        Camera.main.targetTexture = rt;
        uiCamer.Render();
        Camera.main.Render();
        RenderTexture.active = rt;
        var tex = new Texture2D(width, height, TextureFormat.RGB24, false);
        tex.ReadPixels(new Rect(x - 0.5f * width, y - 0.5f * height, width, height), 0, 0);
        //tex.ReadPixels(new Rect(x - 0.5f * w, Screen.height - y - 0.5f * h, w, h), 0, 0);
        tex.Apply(false);
        byte[] fileBytes = tex.EncodeToJPG(80);
        string b64img = Convert.ToBase64String(fileBytes);
        uiCamer.targetTexture = null;
        Camera.main.targetTexture = null;
        RenderTexture.active = null;
        Destroy(rt);
        return new object[] { b64img, "jpg" };
        //return b64img;
    }

    // 输入 定位器列表
    // 返回 物体的text的列表
    [RPC]
    private object GetText(List<object> param)
    {
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        List<List<string>> res = new List<List<string>>();
        int cur = 0;
        while(cur < locatorList.Count)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            res.Add(Locate.GetTextList(targetList));
            cur += 1;
        }
        return res;
    }

    // 输入 定位器列表
    // 返回 物体图像组件的贴图名称的列表
    [RPC]
    private object SetText(List<object> param)
    {
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        int cur = 0;
        while (cur < locatorList.Count)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            Locate.SetTextList(targetList, param[1].ToString());
            cur += 1;
        }
        return null;
    }

    // 输入 定位器列表
    // 返回 滑条组件值的列表
    [RPC]
    private object GetSliderValue(List<object> param)
    {
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        List<List<float>> res = new List<List<float>>();
        int cur = 0;
        while (cur < locatorList.Count)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            res.Add(Locate.GetSliderValueList(targetList));
            cur += 1;
        }
        return res;
    }

    [RPC]
    private object GetDropdownValue(List<object> param)
    {
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        List<List<int>> res = new List<List<int>>();
        int cur = 0;
        while (cur < locatorList.Count)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            List<int> tempRes = new List<int>();
            int i = 0;
            while(i < targetList.Count)
            {
                tempRes.Add(targetList[i].GetComponent<TMP_Dropdown>().value);
                i += 1;
            }
            res.Add(tempRes);
            cur += 1;
        }
        return res;
    }

    [RPC]
    private object SetDropdownValue(List<object> param)
    {
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        int cur = 0;
        while (cur < locatorList.Count)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            int i = 0;
            while(i < targetList.Count)
            {
                targetList[i].GetComponent<TMP_Dropdown>().value = Convert.ToInt32(param[1]);
                i += 1;
            }
            cur += 1;
        }
        return null;
    }


    // 输入 定位器列表
    // 返回 物体名称的列表
    [RPC]
    private object GetName(List<object> param)
    {
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        List<List<string>> res = new List<List<string>>();
        int cur = 0;
        while (cur < locatorList.Count)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            res.Add(Locate.GetNameList(targetList));
            cur += 1;
        }
        return res;
    }

    // 输入 定位器列表
    // 返回 物体图像组件的贴图名称的列表
    [RPC]
    private object GetImgName(List<object> param)
    {
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        List<List<string>> res = new List<List<string>>();
        int cur = 0;
        while (cur < locatorList.Count)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            res.Add(Locate.GetImgNameList(targetList));
            cur += 1;
        }
        return res;
    }

    // 输入 定位器列表
    // 返回 对应的position列表
    // position根据屏幕分辨率进行了归一化
    [RPC]
    public object GetPosition(List<object> param)
    {

        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        List<List<float[]>> res = new List<List<float[]>>();
        int cur = 0;
        while(cur < locatorList.Count)
        {
            Dictionary<string, object> locator = locatorList[cur];
            bool cameraExistFlag = locator.ContainsKey("camera");

            string cameraName = cameraNameDefault;
            if (cameraExistFlag)
            {
                cameraName = locator["camera"].ToString();
            }
            Camera uiCamer = GameObject.Find(cameraName).GetComponent<Camera>();

            bool focusExistFlag = locator.ContainsKey("focus");
            float[] focus = { 0.5f, 0.5f };
            if (focusExistFlag)
            {
                JArray jArray = (JArray)locator["focus"];
                focus = jArray.ToObject<float[]>();
            }
            List<Transform> targetList = Locate.LocateTransform(locator);
            List<float[]> position = Locate.GetPositionList(targetList, screenSize, uiCamer);
            List<float[]> size = Locate.GetSizeList(targetList);
            res.Add(Locate.CorrectPosition(position, size, focus));
            cur += 1;
        }
        return res;
    }

    // 输入 定位器列表
    // 返回 对应的size列表
    // size根据屏幕分辨率进行了归一化
    [RPC]
    public object GetSize(List<object> param)
    {
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        List < List<float[]>> res = new List<List<float[]>>();
        int cur = 0;
        while (cur < locatorList.Count)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            res.Add(Locate.GetSizeList(targetList));
            cur += 1;
        }
        return res;
    }

    // 输入 物体的instanceId
    // 返回 text的值
    // 没找到就返回空字符串
    [RPC]
    private object GetTextById(List<object> param)
    {
        List<List<string>> res = new List<List<string>>();
        JArray jArray = (JArray)param[0];
        List<int> instanceIdList = jArray.ToObject<List<int>>();
        string offspringPath = param[1].ToString();
        int cur = 0;
        while(cur < instanceIdList.Count)
        {
            int instanceId = instanceIdList[cur];
            List<Transform> transformList = Locate.GetTransformListByInstanceID(instanceId, offspringPath);
            res.Add(Locate.GetTextList(transformList));
            cur += 1;
        }
        return res;
    }

    // 输入 物体的instanceId
    // 修改 text的值
    // 找到了text修改完成返回true
    [RPC]
    private object SetTextById(List<object> param)
    {
        JArray jArray = (JArray)param[0];
        List<int> instanceIdList = jArray.ToObject<List<int>>();
        string offspringPath = param[1].ToString();
        string textVal = param[2].ToString();
        int cur = 0;
        while (cur < instanceIdList.Count)
        {
            int instanceId = instanceIdList[cur];
            List<Transform> transformList = Locate.GetTransformListByInstanceID(instanceId, offspringPath);
            Locate.SetTextList(transformList, textVal);
            cur += 1;
        }
        return null;
    }

    // 输入 物体的instanceId
    // 返回 滑条组件的值
    [RPC]
    private object GetSliderValueById(List<object> param)
    {
        List<List<float>> res = new List<List<float>>();
        JArray jArray = (JArray)param[0];
        List<int> instanceIdList = jArray.ToObject<List<int>>();
        string offspringPath = param[1].ToString();
        int cur = 0;
        while (cur < instanceIdList.Count)
        {
            int instanceId = instanceIdList[cur];
            List<Transform> transformList = Locate.GetTransformListByInstanceID(instanceId, offspringPath);
            res.Add(Locate.GetSliderValueList(transformList));
            cur += 1;
        }

        return res;
    }

    // 输入 物体的instanceId
    // 返回 物体的名称
    [RPC]
    private object GetNameById(List<object> param)
    {
        List<List<string>> res = new List<List<string>>();
        JArray jArray = (JArray)param[0];
        List<int> instanceIdList = jArray.ToObject<List<int>>();
        string offspringPath = param[1].ToString();
        int cur = 0;
        while (cur < instanceIdList.Count)
        {
            int instanceId = instanceIdList[cur];
            List<Transform> transformList = Locate.GetTransformListByInstanceID(instanceId, offspringPath);
            res.Add(Locate.GetNameList(transformList));
            cur += 1;
        }
        return res;
    }

    // 输入 物体的instanceId
    // 返回 KnightImage组件的贴图名称
    [RPC]
    private object GetImgNameById(List<object> param)
    {
        List<List<string>> res = new List<List<string>>();
        JArray jArray = (JArray)param[0];
        List<int> instanceIdList = jArray.ToObject<List<int>>();
        string offspringPath = param[1].ToString();
        int cur = 0;
        while (cur < instanceIdList.Count)
        {
            int instanceId = instanceIdList[cur];
            List<Transform> transformList = Locate.GetTransformListByInstanceID(instanceId, offspringPath);
            res.Add(Locate.GetImgNameList(transformList));
            cur += 1;
        }
        return res;
    }

    // 输入 物体的instanceId
    // 返回 归一化后的位置
    [RPC]
    public object GetPositionById(List<object> param)
    {
        List<List<float[]>> res = new List<List<float[]>>();
        JArray jArray = (JArray)param[0];
        List<int> instanceIdList = jArray.ToObject<List<int>>();
        string offspringPath = param[1].ToString();
        string cameraName = param[2].ToString();
        if (cameraName == "")
        {
            cameraName = cameraNameDefault;
        }
        Camera uiCamer = GameObject.Find(cameraName).GetComponent<Camera>();
        int cur = 0;
        while (cur < instanceIdList.Count)
        {
            int instanceId = instanceIdList[cur];
            List<Transform> transformList = Locate.GetTransformListByInstanceID(instanceId, offspringPath);
            
            res.Add(Locate.GetPositionList(transformList, screenSize, uiCamer));
            cur += 1;
        }
        return res;
    }

    // 输入 物体的instanceId
    // 返回 归一化后的大小
    [RPC]
    public object GetSizeById(List<object> param)
    {
        List<List<float[]>> res = new List<List<float[]>>();
        JArray jArray = (JArray)param[0];
        List<int> instanceIdList = jArray.ToObject<List<int>>();
        string offspringPath = param[1].ToString();
        int cur = 0;
        while (cur < instanceIdList.Count)
        {
            int instanceId = instanceIdList[cur];
            List<Transform> transformList = Locate.GetTransformListByInstanceID(instanceId, offspringPath);
            res.Add(Locate.GetSizeList(transformList));
            cur += 1;
        }
        return res;
    }

    // 输入 定位器列表
    // 返回
    [RPC]
    public object GetObjectId(List<object> param)
    {
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        List<List<int>> res = new List<List<int>>();
        int cur = 0;
        while (cur < locatorList.Count)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            res.Add(Locate.GetInstanceIDList(targetList));
            cur += 1;
        }
        return res;
    }



    // 输入 物体的instanceId
    // 返回 子物体的instanceId
    // 子物体可能有多个所以用列表
    [RPC]
    public object GetOffspringIdById(List<object> param)
    {
        List<List<int>> res = new List<List<int>>();
        JArray jArray = (JArray)param[0];
        List<int> instanceIdList = jArray.ToObject<List<int>>();
        string offspringPath = param[1].ToString();
        int cur = 0;
        while (cur < instanceIdList.Count)
        {
            int instanceId = instanceIdList[cur];
            List<Transform> transformList = Locate.GetTransformListByInstanceID(instanceId, offspringPath);
            res.Add(Locate.GetInstanceIDList(transformList));
            cur += 1;
        }
        return res;
    }

    // 输入 物体的instanceId
    // 返回 父物体的instanceId
    [RPC]
    public object GetParentIdById(List<object> param)
    {
        List<List<int>> res = new List<List<int>>();
        JArray jArray = (JArray)param[0];
        List<int> instanceIdList = jArray.ToObject<List<int>>();
        string offspringPath = param[1].ToString();
        int cur = 0;
        while (cur < instanceIdList.Count)
        {
            int instanceId = instanceIdList[cur];
            List<Transform> transformList = Locate.GetTransformListByInstanceID(instanceId, offspringPath);
            List<Transform> parentList = Locate.GetParentTransformList(transformList);
            res.Add(Locate.GetInstanceIDList(parentList));
            cur += 1;
        }
        return res;
    }

    // 输入 物体定位信息的列表
    // 返回 对应的父物体列表
    [RPC]
    public object GetParentId(List<object> param)
    {
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        List<List<int>> res = new List<List<int>>();
        int cur = 0;
        while (cur < locatorList.Count)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            List<Transform> parentList = Locate.GetParentTransformList(targetList);
            res.Add(Locate.GetInstanceIDList(parentList));
            cur += 1;
        }
        return res;
    }


    [RPC]
    private object GetToggleIsOn(List<object> param)
    {
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        List<List<bool>> res = new List<List<bool>>();
        int cur = 0;
        while (cur < locatorList.Count)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            res.Add(Locate.GetToggleIsOnList(targetList));
            cur += 1;
        }
        return res;
    }

    [RPC]
    private object GetToggleIsOnById(List<object> param)
    {
        List<List<bool>> res = new List<List<bool>>();
        JArray jArray = (JArray)param[0];
        List<int> instanceIdList = jArray.ToObject<List<int>>();
        string offspringPath = param[1].ToString();
        int cur = 0;
        while (cur < instanceIdList.Count)
        {
            int instanceId = instanceIdList[cur];
            List<Transform> transformList = Locate.GetTransformListByInstanceID(instanceId, offspringPath);
            res.Add(Locate.GetToggleIsOnList(transformList));
            cur += 1;
        }
        return res;
    }


    [RPC]
    private object SetBtnEnabled(List<object> param)
    {
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        bool enabled = (bool)param[1];
        int cur = 0;
        while (cur < locatorList.Count)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            int i = 0;
            while (i < targetList.Count)
            {
                SetBtnEnabled(targetList[i], enabled);
                i += 1;
            }
            cur += 1;
        }
        return null;
    }

    [RPC]
    private object SetObjectActive(List<object> param)
    {
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        bool active = (bool)param[1];
        int cur = 0;
        while (cur < locatorList.Count)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            int i = 0;
            while (i < targetList.Count)
            {
                targetList[i].gameObject.SetActive(active);
                i += 1;
            }
            cur += 1;
        }
        return null;
    }

    [RPC]
    private object SetObjectActiveById(List<object> param)
    {
        JArray jArray = (JArray)param[0];
        List<int> instanceIdList = jArray.ToObject<List<int>>();
        string offspringPath = param[1].ToString();
        bool active = (bool)param[2];
        int cur = 0;
        while (cur < instanceIdList.Count)
        {
            int instanceId = instanceIdList[cur];
            List<Transform> transformList = Locate.GetTransformListByInstanceID(instanceId, offspringPath);
            int i = 0;
            while (i < transformList.Count)
            {
                transformList[i].gameObject.SetActive(active);
                i += 1;
            }
            cur += 1;
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
        int cur = 0;
        while (cur < transform.childCount)
        {
            Transform childTranform = transform.GetChild(cur);
            SetBtnEnabled(childTranform, enabled);
            cur += 1;
        }
    }

    [RPC]
    private object ClickButton(List<object> param)
    {
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        int cur = 0;
        while (cur < locatorList.Count)
        {
            List<Transform> targetList = Locate.LocateTransform(locatorList[cur]);
            int i = 0;
            while (i < targetList.Count)
            {
                Button button = targetList[i].GetComponent<Button>();
                button.onClick.Invoke();
                i += 1;
            }
            cur += 1;
        }
        return null;
    }

    [RPC]
    private object RayInput(List<object> param)
    {
        Camera uiCamer = GameObject.Find(cameraNameDefault).GetComponent<Camera>();
        List<Dictionary<string, object>> locatorList = Locate.ObjToLocatorList(param);
        Dictionary<string, object> locator = locatorList[0];
        List<Transform> targetList = Locate.LocateTransform(locator);

        string kind = param[1].ToString();
        // 没有定位到就直接返回 
        if (targetList.Count < 1)
        {
            return null;
        }
        Transform target = targetList[0];
        string targetName = target.name;
        bool focusExistFlag = locator.ContainsKey("focus");
        Vector2 size = Vector2.zero;
        Vector2 ScreenVec = Locate.UIPointToScreenPoint(target.position, uiCamer);
        if (focusExistFlag)
        {
            JArray focus = (JArray)locator["focus"];
            float focus_x = focus[0].Value<float>();    // 获取元组的第一个元素
            float focus_y = focus[1].Value<float>();    // 获取元组的第二个元素
            size = target.GetComponent<RectTransform>().sizeDelta;
            ScreenVec[0] = ScreenVec[0] + (0.5f - focus_x) * size[0];
            ScreenVec[1] = ScreenVec[1] + (focus_y - 0.5f) * size[1];
        }
        // 设置点击事件的当前位置
        Vector3 screenPoint = new Vector3(ScreenVec[0], ScreenVec[1], 0f);
        RayInput(screenPoint, targetName, kind);
        return null;
    }

    [RPC]
    private object RayInputById(List<object> param)
    {
        Camera uiCamer = GameObject.Find(cameraNameDefault).GetComponent<Camera>();
        JArray jArray = (JArray)param[0];
        List<int> instanceIdList = jArray.ToObject<List<int>>();
        string offspringPath = param[1].ToString();
        string kind = param[2].ToString();
        int cur = 0;
        while (cur < instanceIdList.Count)
        {
            int instanceId = instanceIdList[cur];
            List<Transform> transformList = Locate.GetTransformListByInstanceID(instanceId, offspringPath);
            if (transformList.Count < 1)
            {
                return null;
            }
            Transform target = transformList[0];
            string targetName = target.name;
            Vector2 ScreenVec = Locate.UIPointToScreenPoint(target.position, uiCamer);
            Vector3 screenPoint = new Vector3(ScreenVec[0], ScreenVec[1], 0f);
            RayInput(screenPoint, targetName, kind);
            cur += 1;
        }
        return null;
    }

    private void RayInput(Vector3 screenPoint, string targetName, string kind)
    {


        // 创建一条从摄像机发射，经过screenPoint的射线
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

    [RPC]
    private object SetTimeScale(List<object> param)
    {
        Time.timeScale = Convert.ToSingle(param[0]); 
        return null;
    }


    [RPC]
    private object SetSendLogFlag(List<object> param)
    {
        sendLogFlag = (bool)param[0];
        return null;
    }

    [RPC]
    private object RegisterPushChannel(List<object> param)
    {
        if (currentRpcClient == null)
            return "fail";
        pendingPushClient = currentRpcClient;
        return "ok";
    }

    void OnEnable(){
        // 注册回调函数
        Application.logMessageReceived += HandleLog;
    }

    void OnDisable()
    {
        // 取消注册回调函数
        Application.logMessageReceived -= HandleLog;
    }

        // 回调函数处理日志信息
    void HandleLog(string logString, string stackTrace, LogType type)
    {
        CsToPython(logString);
    }

}
#endif
