import urllib.request

url = "https://www.kanetsuru.com/wp-content/uploads/2018/02/top06.jpg"
imagefile = "squid.jpg"

urllib.request.urlretrieve(url, imagefile)


print("File Saved")