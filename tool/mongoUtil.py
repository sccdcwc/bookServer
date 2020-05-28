import pymongo
from config import getConfig
class mongoUtil():
    def __init__(self):
        mongoInfo=getConfig("mongo")
        conn_info={
            "host":mongoInfo["MONGO_HOST"],
            "port":mongoInfo["MONGO_PORT"],
            "login":mongoInfo["MONGO_USER"],
            "password":mongoInfo["MONGO_PASSWORD"],
            "database":mongoInfo["MONGO_DB"]
        }
        if conn_info["login"] is None or conn_info["login"] == "":
            self.__client=pymongo.MongoClient("mongodb://{}:{}/".format(conn_info["host"],conn_info["port"]))
        else:
            self.__client=pymongo.MongoClient("mongodb://{}:{}@{}:{}/".format(conn_info["login"],conn_info["password"],conn_info["host"],conn_info["port"]))
        self.__conn=self.__client[conn_info["database"]]

    def getConnect(self):
        return self.__conn