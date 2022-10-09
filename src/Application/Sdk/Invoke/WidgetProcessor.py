import json
import Application.Sdk.Invoke.VendorProcessor as VendorProcessor
import Application.Sdk.Invoke.Dto as Dto


def Create(guid, version, titleBarVisibility, windowVisibility):  # 创建插件
    preference = Dto.WidgetPreference(titleBarVisibility, windowVisibility)
    request = Dto.WidgetCreateRequest(guid, version, preference)
    response = VendorProcessor.InvokeHandler(
        "CreateWidget", "0", Dto.WidgetCreateRequest.ToDict(request))
    value = json.loads(response, object_hook=Dto.WidgetCreateResponse.ToObj)
    return value


def Close():  # 关闭插件
    pass


def Invoke(invoker, methodName, data):  # 调用插件方法
    response = VendorProcessor.InvokeHandler(
        methodName, invoker, data)
    if response == "":
        return ""
    value = json.loads(response, object_hook=Dto.WidgetInvokeResponse.ToObj)
    return value


if __name__ == '__main__':
    value = Create("{E50AB1DF-AAE3-48BA-8819-D3802405F35D}",
                   "1.0.0", "Visible", "Visible")
    print(value.WidgetHandle)
    data = {"Method": "SetSeriesInfo", "Series": [{"SeriesId": "1234", "Name": "SB", "Description": ""}, {
        "SeriesId": "3456", "Name": "ST", "Description": ""}]}
    result = Invoke(value.WidgetHandle, "SetSeriesInfo", data)
    print(result)
