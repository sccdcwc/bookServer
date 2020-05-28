from spider.spiderUtil import searchbook,getbookinfo,getchapterinfo
from model.model import book as bookModel
from tool.mongoUtil import mongoUtil
from model.model import db
def downloadBook(book_name):
    result=bookModel.query.filter_by(name=book_name).first()
    if result:
        return result
    mongodb=mongoUtil().getConnect()
    mongoBookCollection=mongodb["book"]
    result,book_info=searchbook(book_name)
    book=bookModel()
    book.name=book_info["book_name"]
    book.source_url=book_info["book_page"]
    book_info, chapter_list = getbookinfo(book_info)
    book.desc=book_info["book_desc"]
    book.writer=book_info["book_writer"]
    db.session.add(book)
    db.session.commit()
    result,chapter_list=getchapterinfo(chapter_list)
    bookJson=book.to_dict()
    bookJson["chapters"]=chapter_list
    result=mongoBookCollection.insert_one(bookJson)
    return result


if __name__ == '__main__':
    downloadBook("盘龙")