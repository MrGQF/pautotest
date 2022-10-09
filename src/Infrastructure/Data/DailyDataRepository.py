import json
import Infrastructure.Data.DataSet_Daily as daily
import datetime


def GetTestData(code, count, itemKey):
    timeStamps = []
    values = []
    result = daily.QueryByCount(code=code, count=count)
    jsonStr = json.dumps(result)
    for item in json.loads(jsonStr):
        timeStamp = datetime.datetime.utcfromtimestamp(
            item["DateTime"]).strftime("%Y-%m-%d %H:%M:%S")
        timeStamps.append(timeStamp)
        values.append(str(item[itemKey]))
    return (code, timeStamps, values)
