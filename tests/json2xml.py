import json
import os
from pathlib import Path


def json2xml(path: str) -> str:
    head = Path(path).stem
    with open(path, "rb") as f:
        data = json.load(f)
        print(data)

        def recursively_parse(json_data: dict) -> str:
            result = f"<{head}>"
            for key, value in json_data.items():
                temp = f"<{key}>{value}</{key}>"
                result += temp
            result += f"/<{head}>"
            return result

    return recursively_parse(json_data=data)


if __name__ == "__main__":
    print(json2xml("temp.json"))
