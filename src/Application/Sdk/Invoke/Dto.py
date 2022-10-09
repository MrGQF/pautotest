import json


class InvokeRequest:
    def __init__(self, action, actionInstance, actionContext):  # 插件调用请求值
        self.Action = action
        self.ActionInstance = actionInstance
        self.ActionContext = actionContext

    def ToDict(obj):
        return {
            "Action": obj.Action,
            "ActionInstance": obj.ActionInstance,
            "ActionContext": InvokeRequestActionContext.ToDict(obj.ActionContext)
        }


class InvokeRequestActionContext:
    def __init__(self, invoker, function, params):
        self.Invoker = invoker
        self.Function = function
        self.Parameters = params

    def ToDict(obj):
        return {
            "Invoker": obj.Invoker,
            "Function": obj.Function,
            "Parameters": obj.Parameters
        }


class InvokeResponse:
    def __init__(self, action, actionInstance, actionContext):  # 插件调用返回值
        self.Action = action
        self.ActionInstance = actionInstance
        self.ActionContext = actionContext


class InvokeResponseActionContext:
    def __init__(self, res):
        self.Return = res

    def ToObj(str):
        return InvokeResponseActionContext(str["Return"])


class VendorCloseRequest:  # 小核关闭请求值
    def ToDict():
        return {

        }


class WidgetCreateRequest:  # 插件创建请求值
    def __init__(self, guid, version, preference):
        self.WidgetGuid = guid
        self.WidgetVersion = version
        self.WidgetPreference = preference

    def ToDict(obj):
        return {
            "WidgetGuid": obj.WidgetGuid,
            "WidgetVersion": obj.WidgetVersion,
            "WidgetPreference": WidgetPreference.ToDict(obj.WidgetPreference)
        }


class WidgetInvokeRequest:  # 插件调用请求值

    def ToDict(obj):
        return obj


class WidgetInvokeResponse:  # 插件调用返回值
    def __init__(self, Result):
        self.Result = Result

    def ToObj(obj):
        return {
            "Result": obj.Result
        }


class WidgetPreference:  # 插件外观
    def __init__(self, titleBarVisibility, windowVisibility):
        self.TitleBarVisibility = titleBarVisibility
        self.WindowVisibility = windowVisibility

    def ToDict(obj):
        return {
            "TitleBarVisibility": obj.TitleBarVisibility,
            "WindowVisibility": obj.WindowVisibility
        }


class WidgetCreateResponse:  # 插件创建返回值
    def __init__(self, widgetHandle, windowHandle):
        self.WidgetHandle = widgetHandle
        self.WindowHandle = windowHandle

    def ToObj(str):
        return WidgetCreateResponse(str["WidgetHandle"], str["WindowHandle"])


if __name__ == '__main__':
    request = InvokeRequest("action", "instance", "context")
    print(json.dumps(request, default=InvokeRequest.ToDict))

    jsonStr = '{"Action": "action", "ActionInstance": "instance", "ActionContext": "context"}'
    response = json.loads(jsonStr, object_hook=InvokeResponse.ToObj)
    print(response.Action)
