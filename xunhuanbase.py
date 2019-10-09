import base64

p = raw_input("input string to decode:")

while True:
    # Base16
    try:
        print "[?] using base16 deocde"
        n = base64.b16decode(p)
        print "[+] %s" % (n)
        p = n
        continue
    except:
        pass
    # Base32
    try:
        print "[?] using base32 deocde"
        n = base64.b32decode(p)
        print "[+] %s" % (n)
        p = n
        continue
    except:
        pass
    # Base64
    try:
        print "[?] using base64 deocde"
        n = base64.b64decode(p)
        print "[+] %s" % (n)
        p = n
        continue
    except:
        pass
    break
print "[+] flag found : %s" % (n)
