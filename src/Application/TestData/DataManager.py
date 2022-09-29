import json
import sys


def Read():
    with open("./src/Storage/testdata.json") as f:
        result = []
        data = json.load(f)
        result.extend(data["Data"])
        return result


if __name__ == "__main__":
    result = Read()
    print(result)
    print(sys.path)
