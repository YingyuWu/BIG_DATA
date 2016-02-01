#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        word = word.lower()
        word = word.replace(" ","")
        word = word.replace("'","")
        word = word.replace(",","")
        word = word.replace(".","")
        word = word.replace("!","")
        word = word.replace("?","")
        word = word.replace("-","")
        word = word.replace("_","")
        print("%s\t%s" % (word,1))
       

