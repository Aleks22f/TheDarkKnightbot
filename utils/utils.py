import json
import os
import sys


def read_config(path):
    with open(os.path.join(sys.path[0], path), mode="r", encoding="utf-8") as json_data_file:
        config = json.load(json_data_file)
        return config
