def Upper(ch):
    if ch>='A' and ch<='Z':
        return True
def Lower(ch):
    if ch>='a' and ch<='z':
        return True
def rot13(s):
    flag = ''
    for i in s:
        if Upper(i) == True:
             if i>='A' and i<='M':
                 flag += chr(ord(i)+13)
             else:
                 flag += chr(ord(i)-13)
        elif Lower(i) == True:
             if i>='a' and i<='m':
                 flag += chr(ord(i)+13)
             else:
                 flag += chr(ord(i)-13)
        else:
             flag += i
    return flag

if __name__ == "__main__":
    s = 'riny'
    print rot13(s)
