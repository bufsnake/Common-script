import base64

flag = []
for i in range(0,64):
    flag.append(bin(i)[2:].zfill(6))
allbin = ""
for i in flag:
    allbin += i
ans = ''
for i in range(0,len(allbin),8):
    ans += chr(int(allbin[i:i+8],2))
# Usage:
# when not know base64 encode table,we can send ans to server,can dump base64 table
print base64.b64encode(ans)
