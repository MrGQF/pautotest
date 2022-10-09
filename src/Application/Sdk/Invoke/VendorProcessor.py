import json
import Application.Sdk.Invoke.Dto as Dto
import Application.Sdk.Invoke.VendorRuntime as VendorRuntime
import subprocess


def InvokeHandler(funcName, invoker, params):  # 调用小核
    actionContext = Dto.InvokeRequestActionContext(invoker, funcName, params)
    invokeRequest = Dto.InvokeRequest("Invoke", "", actionContext)
    reqDict = json.dumps(invokeRequest, default=Dto.InvokeRequest.ToDict)
    data = VendorRuntime.Invoke("Invoke", reqDict)
    return data


def Start(path, param):  # 启动小核
    cmd = "{path} {param}".format(
        param=param, path=path)
    return subprocess.Popen(args=cmd, shell=False)


def Close():  # 关闭小核
    try:
        InvokeHandler(
            "ShutdownCosmos", "0", Dto.VendorCloseRequest.ToDict())
    except Exception:
        print("关闭小核")


if __name__ == "__main__":
    path = "D:/Code/VSCode/pautotest/vendor/win-x86/Cosmos.Client.Vendor.exe"
    param = "-purl http://localhost:8068 -vurl http://{target} -ppid -1 -wm Offline".format(
        target="localhost:11526")
    Start(path, param)
    Close()
