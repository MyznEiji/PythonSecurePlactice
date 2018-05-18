
import urllib.request

response = urllib.request.urlopen('http://172.21.2.18/blog/wp-admin/')

data = response.read()

print(data)