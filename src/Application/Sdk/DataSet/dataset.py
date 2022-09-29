import ctypes
import os
import time

path = os.path.abspath('./src/Application/Sdk/cosmos.communication.dll')
QueryFunc = ctypes.CDLL(path).Query
QueryFunc.argtypes = [ctypes.c_char_p, ctypes.c_char_p]

StartFunc = ctypes.CDLL(path).Start

PushFunc = ctypes.CDLL(path).Push

value = "test"

if __name__ == '__main__':
    StartFunc()
    QueryFunc(value.encode("utf-8"), value.encode("utf-8"))

    time.sleep(2)
    PushFunc()
    time.sleep(2)
    PushFunc()
