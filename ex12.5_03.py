# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

namelist = list()

url = input('Enter - ')
count = input('Enter count:')
count = int(count)
position = input('Enter position:')
position = int(position)
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
for tag in tags:
    namelist.append(tag.get('href', None))

namelistf = list()
namelistf.append(namelist[position-1])

for i in range(0, count):
    namelist2 = list()
    html2 = urllib.request.urlopen(namelistf[i], context=ctx).read()
    soup2 = BeautifulSoup(html2, 'html.parser')
        # Retrieve all of the anchor tags
    tags2 = soup2('a')
    for tag2 in tags2:
        namelist2.append(tag2.get('href', None))
    namelistf.append(namelist2[position-1])

print("Retrieving:", url)
for i in range(0, len(namelistf)-1):
    print("Retrieving:", namelistf[i])
