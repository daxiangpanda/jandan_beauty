#!/usr/bin/env python
# encoding: utf-8

import urllib2
import os
import random

def url_open(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent',"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11")

    proxies = ['171.38.24.46:8123','182.88.231.145:8123','183.95.81.100:80']
    proxy = random.choice(proxies)

    proxy_support = urllib2.ProxyHandler({'http':proxy})
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)

    response = urllib2.urlopen(url)
    html = response.read()
    return html

def get_page(url):
    html = url_open(url).decode("utf-8")

    a = html.find('current-comment-page')+23
    b = html.find(']',a)
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
    return img_addrs

def save_imgs(folder,img_addrs):
    for each in img_addrs:
        filename = each.split("/")[-1]
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)

def download_mm(folder = "E:\\ooxx",pages = 10):
    os.mkdir(folder)
    os.chdir(folder)

    url = "http://jandan.net/ooxx"
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -=i
        page_url = url+'page-'+str(page_num)+'+comments'
        img_addrs = find_imgs(page_url)
        save_imgs(folder,img_addrs)

if __name__ == '__main__':
    download_mm()