# -*- coding: UTF-8 -*-
import requests
import time
import random

def get_UA():
    UA_list = [
        "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19",
        "Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0",
        "Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"
    ]
    randnum = random.randint(0, len(UA_list)-1)
    h_list = {
        'user-agent': UA_list[randnum]
    }
    return h_list

def get_ip():
    url = 'http://tvp.daxiangdaili.com/ip/?tid=你的订单号&num=1&delay=5&category=2'
    response = requests.get(url)
    response.close()
    proxy = {
        "http":"http://"+response.text
    }
    print(proxy['http'])
    return proxy

if __name__ == '__main__':
    url = 'https://pixel.wp.com/g.gif'
    playload = {
        'v': 'ext',
        'j': '1:5.8',
        'blog': '124283775',
        'post': '158',
        'tz': '8',
        'srv': 'pingxonline.com',
        'host': 'pingxonline.com',
        'ref': 'https://pingxonline.com/',
        'rand': random.random()
    }
    while 1:
        try:
            s = requests.session()
            headers = get_UA()
            proxy = get_ip()
            web_data = s.get(url, headers=headers, proxies=proxy, params=playload)
            print(web_data.content)
            time.sleep(1)
        finally:
            print('error')
