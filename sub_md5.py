#!/usr/bin/env python
import hashlib

def md5(s):
    return hashlib.md5(s).hexdigest()
flag = raw_input("input:")
for i in range(1, 9999999):
    if md5(str(i)).startswith(flag):
	print i
