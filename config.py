import os
from configparser import ConfigParser
import traceback


def getConfig(name,path="config.ini"):
    try:
        config=ConfigParser()
        config.read(path,"utf-8")
        return config[name]
    except Exception:
        traceback.print_exc()


mysqlInfo=getConfig("mysql","config.ini")

class config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True
    MYSQL_HOST = os.environ.get("MYSQL_HOST") if os.environ.get("MYSQL_HOST", None) is not None else mysqlInfo["mysql_host"]
    MYSQL_PORT = os.environ.get("MYSQL_PORT") if os.environ.get("MYSQL_PORT", None) is not None else mysqlInfo["mysql_port"]
    MYSQL_USER = os.environ.get("MYSQL_USER") if os.environ.get("MYSQL_USER", None) is not None else mysqlInfo["mysql_user"]
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD") if os.environ.get("MYSQL_PASSWORD", None) is not None else mysqlInfo["mysql_password"]
    MYSQL_DB = os.environ.get("MYSQL_DATABASE") if os.environ.get("MYSQL_DATABASE", None) is not None else mysqlInfo["mysql_db"]
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}".format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST,
                                                                      MYSQL_PORT, MYSQL_DB)