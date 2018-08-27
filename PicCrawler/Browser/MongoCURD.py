from pymongo import MongoClient


class Connect(object):
    @staticmethod
    def get_connection():
        mongo_url = "127.0.0.1:27017"
        return MongoClient(mongo_url)
