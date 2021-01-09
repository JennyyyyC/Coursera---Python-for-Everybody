import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url: ")
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
#print(data)

info = json.loads(data)
#print(info['comments'])
tot = 0
for item in info['comments']:
    tot = tot + int(item['count'])
print(tot)
