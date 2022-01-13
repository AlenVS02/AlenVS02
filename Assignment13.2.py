import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
input = urllib.request.urlopen(url, context=ctx).read()
treeput = ET.fromstring(input)
lst = treeput.findall('comments/comment')
suma = 0

for item in lst:
    suma += int(item.find('count').text)

print(suma)

