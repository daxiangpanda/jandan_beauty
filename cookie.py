__author__ = '31351'
#!/usr/bin/env python
# encoding: utf-8

import urllib2
import re
from bs4 import BeautifulSoup
n = 1646
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30'
}
req = urllib2.Request(
    url = 'http://jandan.net/ooxx/page-%d#comments'%n,
    headers = headers
)
response = urllib2.urlopen(req)
html = response.read()
soup = BeautifulSoup(html,"html.parser")
print soup
for i in  soup.find_all("div",class_ = 'row'):
    info = []
    for ii in i.children:
        info.append(ii)
    print info

# info[1] name info[1].string;info[3] time str(info[3]).split(">")[-2].split("<")[0];id str(info[4]).split(">")[-3].split("<")[0];
