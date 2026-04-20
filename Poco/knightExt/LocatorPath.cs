#if !WEIXINMINIGAME || UNITY_EDITOR
using UnityEngine;
using System.Text.RegularExpressions;

public class LocatorPath : MonoBehaviour
{
    [HideInInspector]
    public string locatorPath;

    public string elementData;

    public int instanceId;
    private GameObject pocoManager;

    public void RefreshLocatorPath(string path)
    {
        if(path == "")
        {
            locatorPath = this.gameObject.name;
        }
        else
        {
            locatorPath = path + "/" + this.gameObject.name;
        }

        string pythonValidName = GetPythonValidName(this.gameObject.name);

        RectTransform rect = this.GetComponent<RectTransform>();
        if (rect != null)
        {
            elementData = $"{pythonValidName}={{'locator': '{locatorPath}', 'focus': ({rect.pivot.x}, {rect.pivot.y})}}";
        }
        else
        {
            elementData = $"{pythonValidName}={{'locator': '{locatorPath}'}}";
        }

        CallChildrenToRefresh(locatorPath);
    }

    private string GetPythonValidName(string originalName)
    {
        if (string.IsNullOrEmpty(originalName))
            return "_";

        string validName = Regex.Replace(originalName, @"[^a-zA-Z0-9_]", "_");

        if (char.IsDigit(validName[0]))
        {
            validName = "_" + validName;
        }

        return validName;
    }

    private void CallChildrenToRefresh(string path)
    {
        if (pocoManager == null)
        {
            Debug.LogWarning($"LocatorPath: pocoManager is null on '{gameObject.name}', skipping children refresh.");
            return;
        }
        instanceId = this.gameObject.GetInstanceID();
        int childCount = this.transform.childCount;
        int cur = 0;
        while(cur < childCount)
        {
            GameObject child = this.transform.GetChild(cur).gameObject;
            pocoManager.GetComponent<PocoManager>().GetLocatorPathComponent(child, path);
            cur += 1;
        }
    }

    public void AddPocoManager(GameObject gameObject)
    {
        pocoManager = gameObject;
    }
}
#endif