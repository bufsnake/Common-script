import re
import requests
url="http://123.206.87.240:8002/qiumingshan/"
s=requests.Session()
response=s.get(url)
reg=re.compile(r'[0-9+\-*]{3,}[0-9]')
obj=reg.findall(response.text)
data={'value':eval(obj[0])}
reps=s.post(url,data=data)
print(reps.content.decode('utf-8'))
