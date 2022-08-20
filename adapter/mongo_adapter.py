import json
import os
import sys
from pymongo import MongoClient


def init():

    global MONGO_COLLECTION

    mongo_config = get_mongo_config()["mongo_db_configuration"]

    client = MongoClient(host=mongo_config["host"], port=mongo_config["port"])

    database = client[mongo_config["database"]]

    MONGO_COLLECTION = database.get_collection(name=mongo_config["collection"])


def get_mongo_config():
    with open(os.path.join(sys.path[0], "config.json"), mode="r", encoding="utf-8") as json_data_file:
        config = json.load(json_data_file)
        return config
