#!/usr/bin/env python
# encoding: utf-8

import urllib2
import os
import time
import random


def url_open(url):
    req = urllib2.Request(url)
    header1 = 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5'
    header2 = 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5'
    header3 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X; en-us) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53'
    header4 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4'
    header5 = 'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/7.2.1.0 Safari/536.2+'
    header6 = 'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.0.9.2372 Mobile Safari/537.10+'
    header7 = 'Mozilla/5.0 (Linux; Android 4.4.4; en-us; Nexus 5 Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2307.2 Mobile Safari/537.36'
    header8 = 'Mozilla/5.0 (Linux; Android 4.3; Nexus 10 Build/JSS15Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2307.2 Safari/537.36'
    header9 = 'Mozilla/5.0 (Linux; Android 4.3; Nexus 7 Build/JSS15Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2307.2 Safari/537.36'
    header10 = 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)'
    header11 = 'Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13'
    header12 = 'Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    header = [header1,header2,header3,header4,header5,header6,header7,header9,header9,header10,header11,header12]
    req.add_header('User-Agent',random.choice(header))
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
    try:
        html = url_open(url).decode('utf-8')
    except urllib2.HTTPError:
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
    page_num = 1434

    for i in range(1434):
        page_num -=1
        print page_num
        page_url = url+'/page-'+str(page_num)+'#comments'
        img_addrs = find_imgs(page_url)
        print page_url
        save_imgs(folder,img_addrs)
        time.sleep(random.randint(1,7))

if __name__ == '__main__':
    download_mm()