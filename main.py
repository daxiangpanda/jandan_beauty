# encoding: utf-8
__author__ = '31351'
import urllib2
import urllib
import os
from bs4 import BeautifulSoup
def tolist(id):
    with open(path+'list.txt','a') as f:
        f.write(id)
    return True

def inlist(id):
    if id not in list:
        return True

def downloadPic(link,name):
    suffix = '.'+link.split(".")[-1]
    try:
        urllib.urlretrieve(link,path+name+suffix)
    except BaseException, e:
        print e
    print u'已爬pic '+name
    tolist(name.split(".")[0])

if __name__ == '__main__':
    n = 1645
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'}
    path = "C:\\Users\\31351\\PycharmProjects\\jandan_beauty\\pic_beauty\\"
    if os.path.exists(path+'list.txt'):
        with open(path+'list.txt','r') as f:
            list = f.read()
    else:
        f = open(path+'list.txt','a')
    for i in range(n,1,-1):
        req = urllib2.Request(
            url = 'http://i.jandan.net/ooxx/page-%d#comments'%i,
            headers = headers,
            data = None
        )
        response = urllib2.urlopen(req,timeout = 10)
        html = response.read()
        soup = BeautifulSoup(html)
        for i in soup.find_all("li", class_ = 'alt'):
            info = []
            for ii in i.children:
                info.append(ii)
            name = info[1].string
            time = str(info[3]).split(">")[-2].split("<")[0]
            id = str(info[4]).split(">")[-3].split("<")[0]
            link = info[6].find_all("a",class_ = "view_img_link")[0].get("href")
            if not inlist:
                downloadPic(link,id+'.'+name)
            else:
                continue



