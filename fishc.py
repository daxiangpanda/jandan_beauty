#!/usr/bin/env python
# encoding: utf-8

import urllib2
import os
import time
import random


def url_open(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent',r'Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true')
    # proxies = ['120.195.198.69:80','120.195.195.249:80','112.64.28.11:8090']
    # proxy = random.choice(proxies)
    #
    # proxy_support = urllib2.ProxyHandler({'http':proxy})
    # opener = urllib2.build_opener(proxy_support)
    # urllib2.install_opener(opener)
    response = urllib2.urlopen(req)
    html = response.read()
    #print html
    return html


def get_page(url):
    html = url_open(url).decode("utf-8")

    a = html.find('current-comment-page')+23
    b = html.find(']', a)
    return html[a:b]

def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')
    while a!=-1:
        b = html.find('.jpg',a,a+255)
        if b != -1:
            img_addrs.append(html[a+9:b+4])
        else:
            b = a+9
        a = html.find("img src=",b)
    for i in range(len(img_addrs)):
        img_addrs[i] = 'http://'+img_addrs[i].split('http://')[1]
    print img_addrs
    return img_addrs

def save_imgs(folder,img_addrs):
    for each in img_addrs:
        if not each.startswith("http://ww"):
            continue
        filename = each.split("/")[-1]
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)

def download_mm(folder = "E:\\ooxx",pages = 1000):
    if not os.path.exists(folder):
        os.mkdir(folder)
    os.chdir(folder)
    url = "http://i.jandan.net/ooxx"
    page_num = 1599

    for i in range(1555):
        page_num -=1
        print page_num
        page_url = url+'/page-'+str(page_num)+'#comments'
        img_addrs = find_imgs(page_url)
        print page_url
        save_imgs(folder,img_addrs)
        time.sleep(random.randint(1,7))

if __name__ == '__main__':
    download_mm()