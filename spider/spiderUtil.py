import requests
from bs4 import BeautifulSoup
from spider.urls import urls
import traceback
def searchbook(bookname,source="url1"):
    url=urls[source]
    bookurl="{}/s_{}".format(url,bookname)
    response = requests.get(bookurl)
    soup = BeautifulSoup(response.text,'html.parser', from_encoding='utf-8')
    for item in soup.find_all("ul",attrs="list_content"):
        if item.contents[1].text == bookname:
            temp={}
            temp["book_name"]=bookname
            temp["book_page"]=url+item.contents[1].contents[0].attrs["href"]
            return True,temp
    return False,None

def getbookinfo(book):
    url=urls["url1"]
    response = requests.get(book["book_page"])
    soup = BeautifulSoup(response.text,'html.parser', from_encoding='utf-8')
    writer=soup.find("div",attrs="f_l t_c w2").contents[1].text
    book["book_writer"]=writer
    desc=soup.find("div",attrs="desc").text
    book["book_desc"]=desc
    chapterurl = set(())
    chapterlist = []
    for item in soup.find_all("div",attrs="chapter"):
        chapter_name=item.text
        chapter_url=url+item.contents[1].attrs["href"]
        if chapter_url not in chapterurl:
            chapterurl.add(chapter_url)
            temp = {"chapter_name": chapter_name, "chapter_url": chapter_url}
            chapterlist.append(temp)
    return book,chapterlist

def getchapterinfo(chapterlist):
    try:
        newlist=[]
        for chapter in chapterlist:
            response = requests.get(chapter["chapter_url"])
            soup = BeautifulSoup(response.text)
            content=soup.find(id="content")
            if content is not None:
                chapter["chapter_text"]=content.text
                newlist.append(chapter)
                print(chapter)
            else:
                print(chapter["chapter_url"])
        return True,newlist
    except:
        traceback.print_exc()
        return False,None





if __name__ == '__main__':
    result, book_info=searchbook("盘龙")
    book_info,chapter_list=getbookinfo(book_info)
    result,chapter_list=getchapterinfo(chapter_list)
    print(book_info["book_page"])
    print(chapter_list)