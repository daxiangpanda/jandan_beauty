__author__ = '31351'
#!/usr/bin/env python
# encoding: utf-8

import urllib2
import re
from bs4 import BeautifulSoup
n = 1646
headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.122 Mobile Safari/537.36'
}
req = urllib2.Request(
    url = 'http://i.jandan.net/ooxx/page-%d#comments'%n,
    headers = headers
)
response = urllib2.urlopen(req,"html.parser")
html = response.read()
soup = BeautifulSoup(html)
for i in  soup.find_all("li",class_ = 'alt'):
    info = []
    for ii in i.children:
        info.append(ii)
    break
# info[1] name info[1].string;info[3] time str(info[3]).split(">")[-2].split("<")[0];id str(info[4]).split(">")[-3].split("<")[0];
print info[6].find_all("a",class_ = "view_img_link")[0].string

