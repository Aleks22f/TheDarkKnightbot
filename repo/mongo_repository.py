from pymongo import MongoClient
from utils.utils import read_config


class MongoRepository:

    __MONGO_COLLECTION = None

    def __init__(self):
        mongo_config = read_config("config/config.json")["mongo_db_configuration"]

        client = MongoClient(host=mongo_config["host"], port=mongo_config["port"])

        database = client[mongo_config["database"]]

        self.__MONGO_COLLECTION = database.get_collection(name=mongo_config["collection"])