mergeInto(LibraryManager.library, {
  AutomationWS_Connect: function (urlPtr) {
    var url = UTF8ToString(urlPtr);
    try {
      if (typeof Module.__automationWS !== 'undefined' && Module.__automationWS) {
        try { Module.__automationWS.close(); } catch (e) {}
      }
      var ws = new WebSocket(url);
      ws.binaryType = 'arraybuffer';
      Module.__automationWS = ws;
      ws.onopen = function () {
        SendMessage('__AutomationWs__', 'OnWsOpenFromPlugin', '');
      };
      ws.onclose = function () {
        SendMessage('__AutomationWs__', 'OnWsCloseFromPlugin', '');
      };
      ws.onerror = function () {
        SendMessage('__AutomationWs__', 'OnWsCloseFromPlugin', '');
      };
      ws.onmessage = function (ev) {
        if (typeof ev.data !== 'string') return;
        SendMessage('__AutomationWs__', 'OnWsMessageFromPlugin', ev.data);
      };
      return 1;
    } catch (e) {
      return 0;
    }
  },
  AutomationWS_Send: function (msgPtr) {
    var ws = Module.__automationWS;
    if (!ws || ws.readyState !== 1) return 0;
    try {
      ws.send(UTF8ToString(msgPtr));
      return 1;
    } catch (e) {
      return 0;
    }
  },
  AutomationWS_Close: function () {
    var ws = Module.__automationWS;
    if (ws) {
      try { ws.close(); } catch (e) {}
      Module.__automationWS = null;
    }
  },
  AutomationWS_GetReadyState: function () {
    var ws = Module.__automationWS;
    if (!ws) return 3;
    return ws.readyState;
  }
});
