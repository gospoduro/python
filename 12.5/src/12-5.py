#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_115638.html (Sum ends with 1)

import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
#if (len(url) < 1): url = "http://py4e-data.dr-chuck.net/comments_42.html"
if (len(url) < 1): url = "http://py4e-data.dr-chuck.net/comments_115638.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
#
tags = soup('span')
sum = 0
for tag in tags:
    sum=sum+int(tag.contents[0])
print(sum)
