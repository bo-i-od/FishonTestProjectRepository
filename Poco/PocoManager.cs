#if !WEIXINMINIGAME || UNITY_EDITOR
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using Poco;
using System;
using System.IO;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;
using System.Net.Sockets;
using TcpServer;
using UnityEngine;
using Debug = UnityEngine.Debug;



public partial class PocoManager : MonoBehaviour
{
    public const int versionCode = 6;
    public int port = 5001;
    private bool mRunning;
    public AsyncTcpServer server = null;
    private RPCParser rpc = null;
    private SimpleProtocolFilter prot = null;
    private UnityDumper dumper = new UnityDumper();
    private ConcurrentDictionary<string, TcpClientState> inbox = new ConcurrentDictionary<string, TcpClientState>();
    //private VRSupport vr_support = new VRSupport();
    public Queue<string> msgQuene = new Queue<string>();
    public int[] screenSize;
    private TcpClient clientSend;
    private string pushClientKey = null;
    private TcpClient currentRpcClient = null;
    private TcpClient pendingPushClient = null;
    private bool sendLogFlag;
    public string cameraNameDefault;

    // 定义刷新间隔时间
    private float refreshInterval = 5f;
    // 计时器
    private float timer = 0f;

    // Unity 生命周期，每帧调用
    void Update()
    {
        //vr_support.PeekCommand();
        // 每一帧看下消息列表是否有未处理消息
        //ReadMsgQuene();
        HandleAndSendMsg();

        // 累加时间
        timer += Time.deltaTime;

        // 当计时器达到或超过 5 秒时
        if (timer >= refreshInterval)
        {
            // 重置计时器
            timer = 0f;
            
            // 执行刷新逻辑
            RefreshLocator();
        }
    }


    private Dictionary<string, long> debugProfilingData = new Dictionary<string, long>() {
        { "dump", 0 },
        { "screenshot", 0 },
        { "handleRpcRequest", 0 },
        { "packRpcResponse", 0 },
        { "sendRpcResponse", 0 },
    };

    class RPC : Attribute
    {
    }


    void Awake()
    {
        cameraNameDefault = FindFirstObjectByType<Camera>().name;
        screenSize = Locate.GetScreenSize();
        Application.runInBackground = true;
        DontDestroyOnLoad(this);
        prot = new SimpleProtocolFilter();
        rpc = new RPCParser();
        //rpc.addRpcMethod("isVRSupported", vr_support.isVRSupported);
        //rpc.addRpcMethod("hasMovementFinished", vr_support.IsQueueEmpty);
        //rpc.addRpcMethod("RotateObject", vr_support.RotateObject);
        //rpc.addRpcMethod("ObjectLookAt", vr_support.ObjectLookAt);
        rpc.addRpcMethod("GetSDKVersion", GetSDKVersion);
        rpc.addRpcMethod("Dump", Dump);
        rpc.addRpcMethod("GetScreenSize", GetScreenSize);
        rpc.addRpcMethod("GetDebugProfilingData", GetDebugProfilingData);
        addExtRpcMethods();

        mRunning = true;
        sendLogFlag = false;
        this.server = initServer();
        if (this.server == null)
        {
            Debug.LogError(string.Format("Unable to find an unused port from {0} to {1}", port, port + 10));
        }

        //vr_support.ClearCommands();
    }

    AsyncTcpServer initServer()
    {
        AsyncTcpServer s = null;
        for (int i = 0; i < 10; i++)
        {
            s = new AsyncTcpServer(port + i);
            s.Encoding = Encoding.UTF8;

            s.ClientConnected +=
                new EventHandler<TcpClientConnectedEventArgs>(server_ClientConnected);
            s.ClientDisconnected +=
                new EventHandler<TcpClientDisconnectedEventArgs>(server_ClientDisconnected);
            s.DatagramReceived +=
                new EventHandler<TcpDatagramReceivedEventArgs<byte[]>>(server_Received);

            try
            {
                s.Start();
                port = s.Port;
                Debug.Log(string.Format("Tcp server started and listening at {0}", s.Port));
                break;
            }
            catch (SocketException e)
            {
                Debug.Log(string.Format("Tcp server bind to port {0} Failed!", s.Port));
                Debug.Log("--- Failed Trace Begin ---");
                Debug.LogWarning(e);
                Debug.Log("--- Failed Trace End ---");
                s = null;
            }
        }
        return s;
    }

    void server_ClientConnected(object sender, TcpClientConnectedEventArgs e)
    {
        Debug.Log(string.Format("TCP client {0} has connected.",
            e.TcpClient.Client.RemoteEndPoint.ToString()));
    }

    void server_ClientDisconnected(object sender, TcpClientDisconnectedEventArgs e)
    {
        string key = e.TcpClient.Client.RemoteEndPoint.ToString();
        Debug.Log(string.Format("TCP client {0} has disconnected.", key));
        if (key == pushClientKey)
        {
            clientSend = null;
            pushClientKey = null;
            Debug.Log("Push channel disconnected, cleared clientSend.");
        }
    }

    private void server_Received(object sender, TcpDatagramReceivedEventArgs<byte[]> e)
    {
        TcpClientState internalClient = e.Client;
        string tcpClientKey = internalClient.TcpClient.Client.RemoteEndPoint.ToString();
        if (tcpClientKey == pushClientKey)
            return;
        inbox.AddOrUpdate(tcpClientKey, internalClient, (n, o) =>
        {
            return internalClient;
        });
    }


    [RPC]
    private object Dump(List<object> param)
    {
        var onlyVisibleNode = true;
        if (param.Count > 0)
        {
            onlyVisibleNode = (bool)param[0];
        }
        var sw = new Stopwatch();
        sw.Start();
        var h = dumper.dumpHierarchy(onlyVisibleNode);
        debugProfilingData["dump"] = sw.ElapsedMilliseconds;
        return h;
    }



    public static Texture2D ScaleTexture(Texture2D source, int targetWidth, int targetHeight)
    {
        Texture2D result = new Texture2D(targetWidth, targetHeight, source.format, true);
        Color[] rpixels = result.GetPixels(0);
        float incX = ((float)1 / source.width) * ((float)source.width / targetWidth);
        float incY = ((float)1 / source.height) * ((float)source.height / targetHeight);
        for (int px = 0; px < rpixels.Length; px++)
        {
            rpixels[px] = source.GetPixelBilinear(incX * ((float)px % targetWidth),
                incY * ((float)Mathf.Floor(px / targetWidth)));
        }

        result.SetPixels(rpixels, 0);
        result.Apply();
        return result;
    }



    [RPC]
    private object GetScreenSize(List<object> param)
    {
        return new int[] { Screen.width, Screen.height };
    }



    public void stopListening()
    {
        mRunning = false;
        server?.Stop();
    }

    [RPC]
    private object GetDebugProfilingData(List<object> param)
    {
        return debugProfilingData;
    }


    [RPC]
    private object GetSDKVersion(List<object> param)
    {
        return versionCode;
    }



    // 将base64图像保存到指定路径
    public void SavePhotoByString(string base64, string fullPath)
    {

        byte[] buffer = Convert.FromBase64String(base64.Replace(" ", "+"));
        //保存到指定路径
        FileStream fileStream = new FileStream(fullPath, FileMode.OpenOrCreate, FileAccess.ReadWrite, FileShare.ReadWrite)
        {
            Position = 0L
        };
        fileStream.Write(buffer, 0, buffer.Length);
        fileStream.Close();
    }

    void HandleAndSendMsg()
    {
        foreach (TcpClientState client in inbox.Values)
        {
            List<string> msgs = client.Prot.swap_msgs();
            msgs.ForEach(delegate (string msg)
            {
                var sw = new Stopwatch();
                sw.Start();
                var t0 = sw.ElapsedMilliseconds;
                currentRpcClient = client.TcpClient;
                string response = rpc.HandleMessage(msg);
                currentRpcClient = null;
                var t1 = sw.ElapsedMilliseconds;
                byte[] bytes = prot.pack(response);
                var t2 = sw.ElapsedMilliseconds;
                server.Send(client.TcpClient, bytes);
                var t3 = sw.ElapsedMilliseconds;
                debugProfilingData["handleRpcRequest"] = t1 - t0;
                debugProfilingData["packRpcResponse"] = t2 - t1;
                TcpClientState internalClientToBeThrowAway;
                string tcpClientKey = client.TcpClient.Client.RemoteEndPoint.ToString();
                inbox.TryRemove(tcpClientKey, out internalClientToBeThrowAway);
            });
        }

        if (pendingPushClient != null)
        {
            string key = pendingPushClient.Client.RemoteEndPoint.ToString();
            pushClientKey = key;
            clientSend = pendingPushClient;
            pendingPushClient = null;
            Debug.Log($"Push channel activated: {key}");
        }
    }




    void OnApplicationQuit()
    {
        // stop listening thread
        stopListening();
    }

    void OnDestroy()
    {
        // stop listening thread
        stopListening();
    }


}


public class RPCParser
{
    public delegate object RpcMethod(List<object> param);

    protected Dictionary<string, RpcMethod> RPCHandler = new Dictionary<string, RpcMethod>();
    private JsonSerializerSettings settings = new JsonSerializerSettings()
    {
        StringEscapeHandling = StringEscapeHandling.EscapeNonAscii
    };

    public string HandleMessage(string json)
    {
        Dictionary<string, object> data = JsonConvert.DeserializeObject<Dictionary<string, object>>(json, settings);
        if (data.ContainsKey("method"))
        {
            string method = data["method"].ToString();
            List<object> param = null;
            if (data.ContainsKey("params"))
            {
                param = ((JArray)(data["params"])).ToObject<List<object>>();
            }

            object idAction = null;
            if (data.ContainsKey("id"))
            {
                // if it have id, it is a request
                idAction = data["id"];
            }

            string response = null;
            object result = null;
            try
            {
                result = RPCHandler[method](param);
            }
            catch (Exception e)
            {
                // return error response
                Debug.Log(e);
                response = formatResponseError(idAction, null, e);
                return response;
            }

            // return result response
            response = formatResponse(idAction, result);
            return response;

        }
        else
        {
            // do not handle response
            Debug.Log("ignore message without method");
            return null;
        }
    }

    public string formatMessage(string msg, object idAction)
    {
        Dictionary<string, object> data = new Dictionary<string, object>();
        data["jsonrpc"] = "2.0";
        data["msg"] = msg;
        // if idAction is null, it is a notification
        if (idAction != null)
        {
            data["id"] = idAction;
        }
        return JsonConvert.SerializeObject(data, settings);
    }

    // Call a method in the server
    public string formatRequest(string method, object idAction, List<object> param = null)
    {
        Dictionary<string, object> data = new Dictionary<string, object>();
        data["jsonrpc"] = "2.0";
        data["method"] = method;
        if (param != null)
        {
            data["params"] = JsonConvert.SerializeObject(param, settings);
        }
        // if idAction is null, it is a notification
        if (idAction != null)
        {
            data["id"] = idAction;
        }
        return JsonConvert.SerializeObject(data, settings);
    }

    // Send a response from a request the server made to this client
    public string formatResponse(object idAction, object result)
    {
        Dictionary<string, object> rpc = new Dictionary<string, object>();
        rpc["jsonrpc"] = "2.0";
        rpc["id"] = idAction;
        rpc["result"] = result;
        return JsonConvert.SerializeObject(rpc, settings);
    }

    // Send a error to the server from a request it made to this client
    public string formatResponseError(object idAction, IDictionary<string, object> data, Exception e)
    {
        Dictionary<string, object> rpc = new Dictionary<string, object>();
        rpc["jsonrpc"] = "2.0";
        rpc["id"] = idAction;

        Dictionary<string, object> errorDefinition = new Dictionary<string, object>();
        errorDefinition["code"] = 1;
        errorDefinition["message"] = e.ToString();

        if (data != null)
        {
            errorDefinition["data"] = data;
        }

        rpc["error"] = errorDefinition;
        return JsonConvert.SerializeObject(rpc, settings);
    }

    public void addRpcMethod(string name, RpcMethod method)
    {
        RPCHandler[name] = method;
    }


}
#endif