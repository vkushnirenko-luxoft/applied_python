import requests
r=requests.get('http://httpbin.org/ip')
print (r.text)
