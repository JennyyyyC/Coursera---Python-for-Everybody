import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
#print(data.decode())

tree = ET.fromstring(data)
lst = tree.findall('.//count')
#print('count:', len(lst))

tot = 0
for item in lst:
    tot = tot + int(item.text)
print(tot)
