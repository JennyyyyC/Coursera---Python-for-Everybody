from urllib.request import urlopen
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

numlist = list()
# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    for i in tag.contents:
        i = int(i)
    numlist.append(i)
print(sum(numlist))
