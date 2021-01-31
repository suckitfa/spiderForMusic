from sys import set_asyncgen_hooks
import requests
from bs4 import BeautifulSoup
from requests.api import get


def getHTML(url):
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
    resposne = requests.get(url,header)
    if resposne.status_code == 200:
        return resposne.text
    else:
        return "error"

def getFIlE(html):
    soup = BeautifulSoup(html,'lxml')
    items = soup.select('.play-item')
    fileList = []
    for item in items:
        mp3File = item.attrs['data_url']
        prevUrl = "https://demo.dj63.com/"
        fileList.append((prevUrl+mp3File))
        
    return fileList


#获取音乐文件名
# def getFileName(url):
#     return url.split('/').pop()

# 获取mp3文件
def getMp3(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return "error"

# 保存文件
def saveFile(path,url,mp3):
    path += (url.split('/').pop())
    with open(path,('wb')) as file:
        file.write(mp3)

def save_url_as_text(url):
    with open("/Users/bobtang/desktop/music/music.txt","a") as file:
        file.write(url)


if __name__ == "__main__":
    path = "/Users/bobtang/desktop/music/"
    # baseUrl = "https://www.dj63.com/dj/id-66-2.html"
    baseUrls = [
        'https://www.dj63.com/dj/id-4-2.html',
        'https://www.dj63.com/dj/id-4-3.html',
        'https://www.dj63.com/dj/id-4-4.html',
        "https://www.dj63.com/dj/id-41-1.html",
        "https://www.dj63.com/dj/id-41-2.html",
        "https://www.dj63.com/dj/id-41-3.html"
    ]
    i = 1
    for base_url in baseUrls:
        html = getHTML(base_url)
        urls = getFIlE(html)
        for url in urls:
            save_url_as_text(url+"\n")
            i += 1
    print(i)
    # html = getHTML(baseUrl)
    # urls = getFIlE(html)
    # save_url_as_text("fuckyou")
    # for url in urls:
        # mp3 = getMp3(url)
        # if mp3 != "error":
        #     saveFile(path,url,mp3)
        #     print("保存成功")
        # else:
        #     print("失败了！")
        
    # html = getHTML(url)
    # mp3FileList = getFIlE(html)
    # for mp3 in mp3FileList:
    #     print(mp3)
    
