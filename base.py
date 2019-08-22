import string
import base64
my_base64table = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
std_base64table ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
s = "2ifuiJ4F6VMwaY8ATEr7db/="
s = s.translate(string.maketrans(my_base64table,std_base64table))
s = base64.b64decode(s)
flag = list(s)
ss = ""
for i in range(5,len(flag)-1):
    if ord(flag[i]) > 128:
        ss += chr(255-ord(flag[i]))
    else:
        ss += flag[i]
admin = list("flag{}")
print ss
for i in range(0,len(admin)-1):
    print ord(admin[i]) ^ ord(flag[i]),
