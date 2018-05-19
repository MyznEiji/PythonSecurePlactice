"""
If I know the file structure, it is easy to attack
"""

import queue
import threading
import os
import urllib.request
import urllib.error

threads = 10

# $ apachectl start : on terminal
wpurl = "http://192.168.0.8/blog"
localwp = "/var/www/html/blog"
# not need file when attack 
filters = [".jpg", ".gif", ".png", ".css", ".js"]

#move current directory 
os.chdir(localwp)

# all check file's urls
web_paths = queue.Queue()


# os.walk() : get all  files of current postion
for root, directory, files in os.walk("."):
    for file in files:
        # "%s %s" %  (val1, val2) 
        remote_path = "%s/%s" % (root, file)
        
        if remote_path.startswith("."):
            remote_path = remote_path[1:]
            
        
        if os.path.splitext(file)[1] not in  filters:
            web_paths.put(remote_path)
            
def test_remote():
    
    # not empty? 
    while not web_paths.empty():
        path = web_paths.get()
        url = "%s/%s" %  (wpurl, path)
        
        request = urllib.request.Request(url)
        
        
        try:
            response = urllib.request.urlopen(request)
            content =  response.read()
            
            # ex...HTTP response (200, 404, 500...)
            print("[%d] => %s" % (response.code, path))
            
            response.close()
            
            
        except urllib.error.HTTPError as error:
            #print("File get error")
            pass
        
for i in range(threads):
    print("Running  thread: %d" % i)
    t = threading.Thread(target=test_remote)
    t.start()