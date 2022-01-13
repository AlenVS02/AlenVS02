import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')

if len(url) < 1: 
    print('Please Try Again.')
    quit()
input = urllib.request.urlopen(url, context=ctx).read().decode()
json_raw = json.loads(input)
suma = 0 
print(json_raw)

for x in json_raw['comments']:
    suma += int((x['count']))

print(suma)