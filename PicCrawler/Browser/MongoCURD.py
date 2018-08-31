from pymongo import MongoClient
from gridfs import *


class Connect(object):
    def __init__(self, batch_size):
        self.batch_urls = []
        self.batch_files = []
        self.batch_record = []
        self.batch_size = batch_size
        self.batch_count = 0

    @staticmethod
    def get_connection():
        mongo_url = "127.0.0.1:27017"
        return MongoClient(mongo_url)

    def collect_record(self, url, file):
        self.batch_files.append(file)
        self.batch_urls.append(url)
        self.batch_count = self.batch_count + 1
        if self.batch_count == self.batch_size:
            self.insert_batch()

    def insert_batch(self):
        temp_set = {}
        for i in range(len(self.batch_urls)):
            temp_set.setdefault('url', self.batch_urls[i])
            temp_set.setdefault('file', self.batch_files[i])
            print("insert temp_set:")
            print(temp_set)
            client = self.get_connection()
            db = client.phototest
            fs = GridFS(db, collection="images")
            print(self.batch_files[i])
            fs.put(open(self.batch_files[i], 'rb'))
