__author__ = '31351'
#!/usr/bin/env python
# encoding: utf-8

import urllib2
import re
from bs4 import BeautifulSoup
n = 1646
def get_page(html):
    a = html.find('current-comment-page')+23
    b = html.find(']',a)
    return html[a:b]

def find_imgs(html):
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
# info[1] name info[1].string;info[3] time str(info[3]).split(">")[-2].split("<")[0];id str(info[4]).split(">")[-3].split("<")[0];

html = open('E:html.txt','r').read()

a = html.find('current-comment-page')+23
b = html.find(']',a)

print html[3519]
print a
print b
for i in find_imgs(html):
    print i