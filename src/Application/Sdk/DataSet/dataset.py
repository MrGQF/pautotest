import ctypes
import gc
import os
import time
import Application.Sdk.Widget.callback as callback


def Callback(action, method, param):
    print("触发回调:", action, method, param)
    return callback.Agent(action.decode('utf-8'), method.decode('utf-8'), param.decode('utf-8')).encode('utf-8')


def ReleaseCallbackReturn(returnValue):
    print("触发回收: ", returnValue.decode('utf-8'))
    del returnValue
    return


path = os.path.abspath('./src/Application/Sdk/cosmos.communication.dll')
dll = ctypes.CDLL(path)

CChar = ctypes.c_char_p
CPointer = ctypes.c_void_p(None)
CallbackPointer = (ctypes.CFUNCTYPE(CChar, CChar, CChar, CChar))(Callback)
ReleaseCallbackReturnPointer = (
    ctypes.CFUNCTYPE(None, CChar))(ReleaseCallbackReturn)

InitFunc = dll.Init
InitFunc.argtypes = [CPointer, CPointer, CChar, CChar]

PushFunc = dll.Push
PushFunc.argtypes = [CChar]

if __name__ == '__main__':
    processorAddr = "0.0.0.0:8068"
    vendorAddr = "0.0.0.0:9068"
    InitFunc(CallbackPointer, ReleaseCallbackReturnPointer, processorAddr.encode(
        "utf-8"), vendorAddr.encode("utf-8"))

    while (True):
        time.sleep(2)
        pushParam = "{\"Ids\":[\"1\",\"2\"],\"Value\":\"test\"}"
        PushFunc(pushParam.encode("utf-8"))
