import json
from google.protobuf import any_pb2 as AnyPb
from google.protobuf import wrappers_pb2 as WrappersPb

import Infrastructure.Grpc.GrpcChannel as GrpcChannel
import Protos.Common.Common_pb2 as CommonPb
import Protos.Vendor.VendorRuntime_pb2_grpc as VendorRuntimeGrpc

stub = VendorRuntimeGrpc.VendorRuntimeServiceStub(GrpcChannel.vendorChannel)


# 调用小核
def Invoke(type, param):
    typeValue = WrappersPb.StringValue(value=type)
    paramValue = WrappersPb.StringValue(value=param)
    request = CommonPb.InvokeRequest(Type=typeValue, Param=paramValue)
    response = stub.Invoke(request)
    if response.Code != 200:
        raise Exception("请求异常", type, param, response.Code, response.Message)
    data = CommonPb.InvokeResponse()
    AnyPb.Any.Unpack(response.Data, data)

    if data.Data.value == "":
        return ""
    res = json.loads(data.Data.value)
    returnValueJson = json.dumps(res["ActionContext"]["Return"])
    return returnValueJson


if __name__ == '__main__':
    response = Invoke("type", "param")
    print(response)
