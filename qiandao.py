# -*- encoding: utf-8 -*-
data = {'Connection':'close',
        'Content-Length':'0',
        'Accept':'text/plain, */*; q=0.01',
        'Origin':'https://bbs.pediy.com',
        'X-Requested-With':'XMLHttpRequest',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'Referer':'https://bbs.pediy.com/user-tasks-837502-1.htm',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
        'Cookie':'__jsluid_s=05713bdcd2031167ab460288151104d3; bbs_token=KHHw6RldN7kXUaRrskH1C65pGdxb9Ze8I4nG_2FcOvxuSfNvIyPyKHytnjokX6nSpeuMBpSK2g7lXi_2BUjMQnX_2FOxEW_2BrfEVvlXfywAvYk4w675aD0S06VKZiZwR_2FzQGEKNXj8JPWNtA2ZXXwTrQzZ1pg_3D_3D; __utma=153457209.424475175.1566287512.1568705000.1568714362.3; __utmz=153457209.1568714362.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); bbs_sid=13314872fade02eb21f970c13f1e96a5; __utmc=181774708; __utma=181774708.125657486.1565412317.1568985101.1569039241.24; __utmz=181774708.1569039241.24.23.utmcsr=passport.kanxue.com|utmccn=(referral)|utmcmd=referral|utmcct=/user-center-837502.htm; __utmt=1; __utmb=181774708.3.10.1569039241'}

import requests
import os
url = "https://bbs.pediy.com/user-signin.htm"
while True:
    try:
        re = requests.post(url=url,headers=data)
        if len(re.text) == 47:
            print "success",
            print os.system("date")
            break
    except:
        pass
