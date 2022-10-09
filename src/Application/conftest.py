import os
import pytest
import Application.Sdk.Invoke.VendorProcessor as VendorProcessor
import Infrastructure.Grpc.GrpcChannel as GrpcChannel


def StartVendor():
    path = os.path.abspath("./vendor/win-x86/Cosmos.Client.Vendor.exe")
    param = "-purl http://localhost:8068 -vurl http://{target} -ppid -1 -wm offline".format(
        target=GrpcChannel.target)
    pid = VendorProcessor.Start(param=param, path=path)
    return pid.pid


def CloseVendor():
    VendorProcessor.Close()
    print("关闭小核")
    pass


@pytest.fixture(scope="session", autouse=True)
def init_session():   # 初始化 会话
    pid = StartVendor()
    yield pid
    CloseVendor()


@pytest.fixture(scope='module')
def init_module(init_session):  # 初始化模块
    pid = init_session
    yield pid
