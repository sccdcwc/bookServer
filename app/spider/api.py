from . import spider
from flask import jsonify,request
from app.spider.view import *
def reformat(data=None, code=200, message=None):
    temp = {
        "code": 200,
        "message": "接口调用成功",
    }
    if message is not None:
        temp["message"] = message
    if code is not 200:
        temp["code"] = code
    if data is not None:
        for key, value in data.items():
            temp[key] = value
    return jsonify(temp)

@spider.route("/spider/book",methods=["GET"])
def IdownloadBook():
    book_name=request.args.get("book_name",None)
    if book_name is not None:
        result=downloadBook(book_name)
    return reformat(data=True,code=200,message="爬取成功")