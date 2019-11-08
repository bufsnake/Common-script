# -*- coding: utf-8 -*-

from collections import Counter

f=open('md5.java','r')

f_read=f.read()

print Counter(f_read)
