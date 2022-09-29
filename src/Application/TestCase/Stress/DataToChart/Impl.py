import Application.TestCase.Stress.Base as Base
import Application.Sdk.Widget.DataToChart as DataToChart


def SetDataByDaily(widgetHandle, code, timeStamps, values):
    print(len(values))
    data = {
        "Method": "SetData",
        "TimeStamp": timeStamps,
        "Series": [
            {
                "SeriesId": code,
                "Fields": [
                    {
                        "FieldId": "Open",
                        "Values": values,
                        "Tips": ["", ""],
                    }
                ]
            }
        ]
    }
    DataToChart.SetData(widgetHandle, data)


def SetFields(WidgetHandle, seriesId):
    # 设置线信息
    data = {"Method": "SetSeriesInfo", "Series": [
        {"SeriesId": seriesId, "Name": seriesId, "Description": "日线数据"}]}
    DataToChart.SetSeries(WidgetHandle, data)

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
    DataToChart.SetFieldInfo(WidgetHandle, data)

    # 设置预选中字段
    data = [seriesId]
    DataToChart.SetPreSelectFields(WidgetHandle, "Open", data)


class StressImpl(Base.StressProcessor):
    def Init(self, widgetHandle, param):
        SetFields(widgetHandle, param)

    def Recover(self, widgetHandle, param):
        SetDataByDaily(widgetHandle=widgetHandle, code=param[0],
                       timeStamps=param[1], values=param[2])

    def Process(self, widgetHandle, param):
        SetDataByDaily(widgetHandle=widgetHandle, code=param[0],
                       timeStamps=param[1], values=param[2])
