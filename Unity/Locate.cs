using System.Collections.Generic;
using System.Text.RegularExpressions;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
using Newtonsoft.Json;
public class Locate
{


    // ???? ???????
    // ??? ???Transform????
    public static List<Transform> LocateTransform(Dictionary<string, object> locators)
    {
        string[] locatorArray;
        bool locatorExistFlag = locators.ContainsKey("locator");
        bool offspring_locatorExistFlag = locators.ContainsKey("offspring_locator");
        List<Transform> transformList = new List<Transform>();
        if (locatorExistFlag)
        {

            transformList = GetChildTransformList(transformList);
            locatorArray = locators["locator"].ToString().Split('/');
            // ??????????
            GameObject rootGameObject = GameObject.Find(locatorArray[0]);
            if (rootGameObject == null)
            {
                return transformList;
            }
            Transform rootTranform = rootGameObject.transform;
            GetTransformListByChild(locatorArray, rootTranform, ref transformList);
            return transformList;
        }
        else if (offspring_locatorExistFlag)
        {
            transformList = GetChildTransformList(transformList);
            locatorArray = locators["offspring_locator"].ToString().Split('/');
            GetTransformListByOffspring(locatorArray, ref transformList);
            return transformList;
        }
        return transformList;
    }


    // ????Transform????
    // ????????????Transform????
    public static List<Transform> GetChildTransformList(List<Transform> transformList)
    {
        if (transformList.Count == 0)
        {
            return transformList;
        }
        List<Transform> transformListNew = new List<Transform>();
        int transformListCount = transformList.Count;
        int cur = 0;
        while (cur < transformListCount)
        {
            AddChildren(transformList[cur], ref transformListNew);
            cur += 1;
        }
        return transformListNew;
    }

    // ????Transform????
    // ????????????Transform????
    public static List<Transform> GetOffspringTransformList(List<Transform> transformList, string offspringName)
    {
        if (transformList.Count == 0)
        {
            return transformList;
        }
        int transformListCount = transformList.Count;
        int cur = 0;
        while (cur < transformListCount)
        {
            transformList[cur] = FindChildRecursively(transformList[cur], offspringName);
            cur += 1;
        }
        return transformList;
    }

    // ????Transform????
    // ????????????Transform????
    public static List<Transform> GetParentTransformList(List<Transform> transformList)
    {
        if (transformList.Count == 0)
        {
            return transformList;
        }
        int transformListCount = transformList.Count;
        int cur = 0;
        while (cur < transformListCount)
        {
            transformList[cur] = transformList[cur].parent;
            cur += 1;
        }
        return transformList;
    }

    //???? Transform
    //???? ?????????Transform????
    private static void AddChildren(Transform parent, ref List<Transform> transformListNew)
    {
        int childCount = parent.childCount;
        int childIndex = 0;
        while (childIndex < childCount)
        {
            Transform child = parent.GetChild(childIndex);
            childIndex += 1;
            //???????????
            if (!child.gameObject.activeInHierarchy)
            {
                continue;
            }
            transformListNew.Add(child);
        }
    }
    private static int? GetNumberInBrackets(string str)
    {
        Match match = Regex.Match(str, @"\[(\d+)\]$");
        if (match.Success)
        {
            return int.Parse(match.Groups[1].Value);
        }
        return null;
    }

    // ????locatorArray[]????????????
    public static void GetTransformListByChild(string[] locatorArray, Transform rootTransform, ref List<Transform> transformList)
    {
        int index = 0;
        int locatorArrayLen = locatorArray.Length;
        // ???????????????????

        transformList.Add(rootTransform);
        if (locatorArrayLen > 0 && rootTransform.name == locatorArray[0])
        {
            index += 1;
        }

        while (index < locatorArrayLen)
        {
            string currentLocator = locatorArray[index];
            int? numberInBrackets = GetNumberInBrackets(currentLocator);

            // ??? locator ???????????????Transform
            if (currentLocator == "")
            {
                transformList = GetChildTransformList(transformList);
                index += 1;
                continue;
            }
            if (numberInBrackets == null)
            {
                transformList = UpdateTransformListByChild(currentLocator, transformList);
                index += 1;
                continue;
            }
            string realName = Regex.Replace(currentLocator, @"\[\d+\]$", "");
            if (realName != "")
            {
                transformList = UpdateTransformListByChild(realName, transformList, numberInBrackets.Value);
                index += 1;
                continue;
            }
            List<Transform> result = new List<Transform>();
            foreach (Transform parent in transformList)
            {
                List<Transform> activeChildren = new List<Transform>();
                for (int i = 0; i < parent.childCount; i++)
                {
                    Transform child = parent.GetChild(i);
                    if (child.gameObject.activeInHierarchy)
                        activeChildren.Add(child);
                }
                if (numberInBrackets.Value < activeChildren.Count)
                    result.Add(activeChildren[numberInBrackets.Value]);
            }
            transformList = result;
            index += 1;
        }
        // ?????????
    }

    // ????locatorArray[]????????????
    private static void GetTransformListByOffspring(string[] locatorArray, ref List<Transform> transformList)
    {
        int index = 0;
        int locatorArrayLen = locatorArray.Length;
        if (transformList.Count == 0)
        {
            transformList.Add(GameObject.Find(locatorArray[0]).transform);
            index = 1;
        }
        while (index < locatorArrayLen)
        {
            if (locatorArray[index] == "")
            {
                transformList = GetChildTransformList(transformList);
                index += 1;
                continue;
            }
            UpdateTransformListByOffspring(locatorArray[index], ref transformList);
            index += 1;
        }
    }

    // ????locator??????????????????????? 
    private static List<Transform> UpdateTransformListByChild(string locator, List<Transform> transformList)
    {
        List<Transform> resList = new List<Transform>();
        int transformListCount = transformList.Count;
        int cur = 0;
        while (cur < transformListCount)
        {
            int childCount = transformList[cur].childCount;
            int i = 0;
            while (i < childCount)
            {
                Transform childTransform = transformList[cur].GetChild(i);
                if (childTransform == null || !childTransform.gameObject.activeInHierarchy)
                {
                    i += 1;
                    continue;
                }
                if (childTransform.name != locator)
                {
                    i += 1;
                    continue;
                }
                resList.Add(childTransform);
                i += 1;
            }
            cur += 1;
        }
        return resList;
    }

    //private static void UpdateTransformListByChild(string locator, ref List<Transform> transformList, int childIndex)
    //{
    //    int transformListCount = transformList.Count;
    //    int cur = 0;

    //    while (cur < transformListCount)
    //    {
    //        int i = 0;
    //        int index = 0;
    //        bool isFind = false;
    //        while(i < transformList[cur].childCount)
    //        {
    //            Transform childTransform = transformList[cur].GetChild(i);
    //            bool isTargetName = childTransform.name == locator;
    //            bool isActivated = childTransform.gameObject.activeSelf;
    //            if (!(isTargetName && isActivated))
    //            {
    //                i += 1;
    //                continue;
    //            }
    //            if (childIndex == index)
    //            {
    //                transformList[cur] = childTransform;
    //                isFind = true;
    //            }
    //            index += 1;
    //            i += 1;
    //        }
    //        if (!isFind)
    //        {
    //            transformList.Remove(transformList[cur]);
    //            cur -= 1;
    //            transformListCount -= 1;
    //        }
    //        cur += 1;
    //    }
    //}

    private static List<Transform> UpdateTransformListByChild(string locator, List<Transform> transformList, int childIndex)
    {
        List<Transform> resList = new List<Transform>();
        int cur = 0;
        while (cur < transformList.Count)
        {
            int childCount = transformList[cur].childCount;
            int i = 0;
            int matchCount = 0;
            while (i < childCount)
            {
                Transform childTransform = transformList[cur].GetChild(i);
                if (childTransform == null || !childTransform.gameObject.activeInHierarchy)
                {
                    i += 1;
                    continue;
                }
                if (childTransform.name != locator)
                {
                    i += 1;
                    continue;
                }
                if (matchCount == childIndex)
                {
                    resList.Add(childTransform);
                    break;
                }
                matchCount += 1;
                i += 1;
            }
            cur += 1;
        }
        return resList;
    }

    // ????locator?????????????????????????
    private static void UpdateTransformListByOffspring(string locator, ref List<Transform> transformList)
    {
        int cur = 0;
        int transformListCount = transformList.Count;
        while (cur < transformListCount)
        {


            Transform offspringTransform = FindChildRecursively(transformList[cur], locator);
            if (offspringTransform == null || !offspringTransform.gameObject.activeInHierarchy)
            {
                transformList.Remove(transformList[cur]);
                cur -= 1;
                transformListCount -= 1;
            }
            else
            {
                transformList[cur] = offspringTransform;
                Debug.Log("curTransform:" + transformList[cur].name);
            }
            cur += 1;
        }
    }

    public static Transform FindTransformByPath(string path)
    {
        if (string.IsNullOrEmpty(path))
        {
            return null;
        }

        string[] parts = path.Split('/');
        List<string> segments = new List<string>();
        for (int i = 0; i < parts.Length; i++)
        {
            if (parts[i].Length > 0) segments.Add(parts[i]);
        }
        
        if (segments.Count == 0)
        {
            return null;
        }

        GameObject root = GameObject.Find(segments[0]);
        if (root == null)
        {
            return null;
        }

        if (segments.Count == 1)
        {
            return root.transform;
        }

        return root.transform.Find(string.Join("/", segments.GetRange(1, segments.Count - 1).ToArray()));
    }

    public static List<Dictionary<string, object>> ObjToLocatorList(List<object> param)
    {
        List<Dictionary<string, object>> locatorList;

        var objstr = JsonConvert.SerializeObject(param[0]);
        //string(json) ? Dictionary
        locatorList = JsonConvert.DeserializeObject<List<Dictionary<string, object>>>(objstr);
        return locatorList;
    }

    public static List<string> GetImgNameList(List<Transform> targetList)
    {
        List<string> imgNameList = new List<string>();
        foreach (Transform target in targetList)
        {
            if (target.TryGetComponent(out KnightImage knightImage))
            {
                imgNameList.Add(knightImage.sprite.name);
                continue;
            }
            if (target.TryGetComponent(out Image image))
            {
                imgNameList.Add(image.sprite.name);
                continue;
            }
        }
        return imgNameList;
    }

    public static List<float> GetSliderValueList(List<Transform> targetList)
    {
        List<float> sliderValueList = new List<float>();
        foreach (Transform target in targetList)
        {
            sliderValueList.Add(target.GetComponent<Slider>().value);
        }
        return sliderValueList;
    }

    public static List<string> GetTextList(List<Transform> targetList)
    {
        List<string> textList = new List<string>();
        foreach (Transform target in targetList)
        {
            if (target.TryGetComponent(out TextMeshProUGUI tmpUGUI))
            {
                textList.Add(tmpUGUI.text);
                continue;
            }
            if (target.TryGetComponent(out TMP_InputField tmpInputField))
            {
                textList.Add(tmpInputField.text);
                continue;
            }
            if (target.TryGetComponent(out InputField inputField))
            {
                textList.Add(inputField.text);
                continue;
            }

        }
        return textList;
    }

    public static void SetTextList(List<Transform> targetList, string text)
    {
        foreach (Transform target in targetList)
        {
            if (target.TryGetComponent(out TextMeshProUGUI tmpUGUI))
            {
                tmpUGUI.text = text;
                continue;
            }
            if (target.TryGetComponent(out TMP_InputField tmpInputField))
            {
                tmpInputField.text = text;
                continue;
            }
            if (target.TryGetComponent(out InputField inputField))
            {
                inputField.text = text;
                continue;
            }
        }
    }

    public static List<string> GetNameList(List<Transform> targetList)
    {
        List<string> nameList = new List<string>();
        foreach (Transform target in targetList)
        {
            nameList.Add(target.name);
        }
        return nameList;
    }

    public static List<float[]> GetPositionList(List<Transform> targetList, int[] screenSize, Camera cam)
    {
        List<float[]> positionList = new List<float[]>();
        foreach (Transform target in targetList)
        {
            Vector2 screenVec = TransformToScreenPoint(target, cam);
            float[] normalized = new float[2];
            normalized[0] = screenVec.x / screenSize[0];
            normalized[1] = 1f - screenVec.y / screenSize[1];
            positionList.Add(normalized);
        }
        return positionList;
    }

    public static List<float[]> GetSizeList(List<Transform> targetList)
    {
        List<float[]> sizeList = new List<float[]>();
        int[] screenSize = GetScreenSize();
        foreach (Transform target in targetList)
        {
            RectTransform rt = target.GetComponent<RectTransform>();
            if (rt != null)
            {
                Vector2 size = rt.rect.size;
                sizeList.Add(new float[] { size.x / screenSize[0], size.y / screenSize[1] });
            }
            else
            {
                sizeList.Add(new float[] { 0f, 0f });
            }
        }
        return sizeList;
    }

    public static List<int> GetInstanceIDList(List<Transform> targetList)
    {
        List<int> instanceIDList = new List<int>();
        foreach (Transform target in targetList)
        {
            // ??????????instanceID
            if (!target.gameObject.activeInHierarchy)
            {
                continue;
            }
            instanceIDList.Add(target.gameObject.GetInstanceID());
        }
        return instanceIDList;
    }

    public static List<bool> GetToggleIsOnList(List<Transform> targetList)
    {
        List<bool> toggleIsOnList = new List<bool>();
        foreach (Transform target in targetList)
        {
            toggleIsOnList.Add(target.GetComponent<Toggle>().isOn);
        }
        return toggleIsOnList;
    }



    public static int[] GetScreenSize()
    {
        return new int[] { Screen.width, Screen.height };
    }

    public static Vector2 GetCanvasReferenceResolution()
    {
        GameObject UICanvas = GameObject.Find("UICanvas");
        if (UICanvas == null)
        {
            return new Vector2(1, 1);
        }
        CanvasScaler canvasScaler = UICanvas.GetComponent<CanvasScaler>();
        return canvasScaler.referenceResolution;
    }

    /// <summary>
    /// Converts a Transform's position to screen coordinates.
    /// Uses RectTransformUtility for UI elements (RectTransform),
    /// uses Camera.WorldToScreenPoint for 3D objects (plain Transform).
    /// </summary>
    public static Vector2 TransformToScreenPoint(Transform target, Camera cam)
    {
        if (target.GetComponent<RectTransform>() != null)
        {
            return RectTransformUtility.WorldToScreenPoint(cam, target.position);
        }
        Vector3 sp = cam.WorldToScreenPoint(target.position);
        return new Vector2(sp.x, sp.y);
    }

    /// <summary>
    /// Legacy UI-only conversion, kept for backward compatibility.
    /// Prefer TransformToScreenPoint for new code.
    /// </summary>
    public static Vector2 UIPointToScreenPoint(Vector3 worldPoint, Camera uiCamera)
    {
        return RectTransformUtility.WorldToScreenPoint(uiCamera, worldPoint);
    }

    // ???????? ??????poco??offspring
    public static Transform FindChildRecursively(Transform parent, string name)
    {
        Transform t;
        t = parent.Find(name);
        if (t == null)
        {
            foreach (Transform tran in parent)
            {
                t = FindChildRecursively(tran, name);
                if (t != null)
                {
                    return t;
                }
            }
        }
        return t;
    }

    public static List<Transform> GetTransformListByInstanceID(int instanceID, string offspringPath)
    {
        List<Transform> transformList = new List<Transform>();
        int cur = 0;

        Transform targetTransform = GetTransformByInstanceID(instanceID);
        if (targetTransform == null)
        {
            return transformList;
        }
        transformList.Add(targetTransform);

        string[] locatorArray = offspringPath.Split('>');
        // ???locator????????
        if (locatorArray.Length == 1 && locatorArray[0] == "")
        {
            return transformList;
            //string[] result = new string[locatorArray.Length - 1];
            //Array.Copy(locatorArray, 1, result, 0, locatorArray.Length - 1);
            //locatorArray = result;
        }
        cur = 0;
        while (cur < locatorArray.Length)
        {
            string currentLocator = locatorArray[cur];
            int? numberInBrackets = GetNumberInBrackets(currentLocator);

            // ??? locator ???????????????Transform
            if (currentLocator == "")
            {
                transformList = GetChildTransformList(transformList);
                cur += 1;
                continue;
            }
            if (numberInBrackets == null)
            {
                transformList = UpdateTransformListByChild(currentLocator, transformList);
                cur += 1;
                continue;
            }
            string realName = Regex.Replace(currentLocator, @"\[\d+\]$", "");
            if (realName != "")
            {
                transformList = UpdateTransformListByChild(realName, transformList, numberInBrackets.Value);
                cur += 1;
                continue;
            }
            List<Transform> result = new List<Transform>();
            foreach (Transform parent in transformList)
            {
                List<Transform> activeChildren = new List<Transform>();
                for (int i = 0; i < parent.childCount; i++)
                {
                    Transform child = parent.GetChild(i);
                    if (child.gameObject.activeInHierarchy)
                        activeChildren.Add(child);
                }
                if (numberInBrackets.Value < activeChildren.Count)
                    result.Add(activeChildren[numberInBrackets.Value]);
            }
            transformList = result;
            cur += 1;
        }
        return transformList;
    }

    public static Transform GetTransformByInstanceID(int instanceID)
    {
        foreach (var go in GameObject.FindObjectsOfType<GameObject>())
        {
            if (go.GetInstanceID() != instanceID)
            {
                continue;
            }
            if (!go.activeInHierarchy)
            {
                break;
            }
            return go.transform;
        }
        return null;
    }

    public static List<float[]> CorrectPosition(List<float[]> positionList, List<float[]> sizeList, float[] focus)
    {
        float biasX = 0.5f - focus[0];
        float biasY = 0.5f - focus[1];
        List<float[]> res;
        res = new List<float[]>();
        int cur = 0;
        while (cur < positionList.Count)
        {
            res.Add(new float[] { positionList[cur][0] + sizeList[cur][0] * biasX, positionList[cur][1] + sizeList[cur][1] * biasY });
            cur += 1;
        }
        return res;
    }





    public static List<Dictionary<string, object>> GetScrollViewInfoList(
        List<Transform> targetList, int[] screenSize, Camera cam, float[] focus)
    {
        List<float[]> positionList = GetPositionList(targetList, screenSize, cam);
        List<float[]> sizeList = GetSizeList(targetList);
        List<float[]> correctedPositionList = CorrectPosition(positionList, sizeList, focus);

        List<Dictionary<string, object>> result = new List<Dictionary<string, object>>();

        for (int cur = 0; cur < targetList.Count; cur++)
        {
            Transform target = targetList[cur];

            ScrollRect scrollRect = target.GetComponent<ScrollRect>();
            if (scrollRect == null)
            {
                Transform search = target.parent;
                while (search != null)
                {
                    scrollRect = search.GetComponent<ScrollRect>();
                    if (scrollRect != null) break;
                    search = search.parent;
                }
            }

            if (scrollRect == null)
            {
                result.Add(new Dictionary<string, object>());
                continue;
            }

            List<int> contentChildrenIds = new List<int>();
            float[] firstChildSize = null;

            if (scrollRect.content != null)
            {
                for (int i = 0; i < scrollRect.content.childCount; i++)
                {
                    Transform child = scrollRect.content.GetChild(i);
                    if (child.gameObject.activeInHierarchy)
                    {
                        contentChildrenIds.Add(child.gameObject.GetInstanceID());
                    }
                }

                if (contentChildrenIds.Count > 0)
                {
                    Transform firstChild = GetTransformByInstanceID(contentChildrenIds[0]);
                    if (firstChild != null)
                    {
                        List<float[]> fcs = GetSizeList(new List<Transform> { firstChild });
                        if (fcs.Count > 0) firstChildSize = fcs[0];
                    }
                }
            }

            bool isElastic = scrollRect.movementType == ScrollRect.MovementType.Elastic;

            Dictionary<string, object> info = new Dictionary<string, object>
            {
                { "instanceId", target.gameObject.GetInstanceID() },
                { "horizontal", scrollRect.horizontal },
                { "vertical", scrollRect.vertical },
                { "elastic", isElastic },
                { "elasticity", scrollRect.elasticity },
                { "inertia", scrollRect.inertia },
                { "decelerationRate", scrollRect.decelerationRate },
                { "position", correctedPositionList[cur] },
                { "size", sizeList[cur] },
                { "contentChildrenIds", contentChildrenIds },
                { "firstChildSize", firstChildSize },
            };
            result.Add(info);
        }
        return result;
    }
}
