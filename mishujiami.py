a="109930883401687215730636522935643539707"
a=a.split("0")
flag=''
for i in range(0,len(a)):
     str = a[i]
     list=[]
     sum=0
     for j in str:
        list.append(j)
        length = len(list)
     for k in range(0,length):
        sum+=int(list[k])
     print sum % 26
     flag += chr((sum % 26+65)) + ''
print flag
