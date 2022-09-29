import Application.Sdk.Invoke.WidgetProcessor as WidgetProcessor
import Infrastructure.Grpc.GrpcChannel as GrpcChannel
import Application.Sdk.Invoke.VendorProcessor as VendorProcessor


def SetSeries(widgetHandle, data):
    WidgetProcessor.Invoke(widgetHandle, "SetSeriesInfo", data)
    return


def SetFieldInfo(widgetHandle, data):
    WidgetProcessor.Invoke(widgetHandle, "SetFieldInfo", data)


def SetData(widgetHandle, data):
    WidgetProcessor.Invoke(widgetHandle, "SetData", data)


def SetPreSelectFields(widgetHandle, fieldId, seriesIds):
    data = {
        "Method": "SetPreSelectFields",
        "PreSelectFields": [
            {
                "FieldId": fieldId,
                "SeriesId": seriesIds
            }
        ]
    }
    WidgetProcessor.Invoke(widgetHandle, "SetPreSelectFields", data)


if __name__ == '__main__':
    WidgetHandle = 0
    Code = "USHA600000"

    # 启动小核
    path = "D:/Desktop/Cosmos.Client.Vendor.exe"
    param = "-purl http://localhost:8068 -vurl http://{target} -ppid -1 -wm Offline".format(
        target=GrpcChannel.target)
    pid = VendorProcessor.Start(param=param, path=path)
    print(pid)

    # 创建图表插件
    value = WidgetProcessor.Create("{E50AB1DF-AAE3-48BA-8819-D3802405F35D}",
                                   "1.0.0", "Visible", "Visible")
    WidgetHandle = value.WidgetHandle
    print("\n ####################################", WidgetHandle)

    # 设置线信息
    data = {"Method": "SetSeriesInfo", "Series": [
        {"SeriesId": Code, "Name": Code, "Description": "日线数据"}]}
    result = SetSeries(WidgetHandle, data)

    # 设置属性信息
    data = {
        "Method": "SetFieldInfo",
        "Fields": [
            {
                "FieldId": "Open",
                "Name": "Open",
                "Describe": "开盘价",
                "Unit": "元",
                "DataType": "double"
            },
            {
                "FieldId": "High",
                "Name": "High",
                "Describe": "最高价",
                "Unit": "元",
                "DataType": "double"
            },
            {
                "FieldId": "Low",
                "Name": "Low",
                "Describe": "最低价",
                "Unit": "元",
                "DataType": "double"
            },
            {
                "FieldId": "Close",
                "Name": "Close",
                "Describe": "收盘价",
                "Unit": "元",
                "DataType": "double"
            }
        ]
    }
    result = SetFieldInfo(WidgetHandle, data)

    # 设置 数据
    data = {
        "Method": "SetData",
        "TimeStamp": ["2021-01-01", "2021-01-02"],
        "Series": [
            {
                "SeriesId": Code,
                "Fields": [
                    {
                        "FieldId": "Open",
                        "Values": ["1", "2"],
                        "Tips": ["", ""],
                    }
                ]
            }
        ]
    }
    SetData(WidgetHandle, data)
