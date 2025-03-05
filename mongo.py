import pymongo
from pymongo import MongoClient


class BancoMongo:
    def __init__(self):
        self.__conexao = MongoClient("localhost", 27017)
        self.db_teste = self.__conexao["db_teste"]

    def get_database(self):
        return self.db_teste




