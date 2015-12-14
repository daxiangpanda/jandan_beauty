#!/usr/bin/env python
# encoding: utf-8
from bs4 import BeautifulSoup

f = open(r'C:\Users\31351\PycharmProjects\jandan_beauty\html.txt','r')
html = f.read()
soup = BeautifulSoup(html)
for i in soup.find_all("li",class_ = "alt"):
    info = []
    for ii in i.children:
        info.append(ii)
    break

print info[1].string
