#!/usr/bin/env python3

import sys

BREAK = "###"

k = 0

ngram = [BREAK,BREAK,BREAK]

for line in sys.stdin:
    line = line.replace("~","-")
    words = line.split()
    words.append(BREAK)
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
        ngram.append(word)
        ngram = ngram[1:]
        data = "~".join(ngram)
        print("%s\t%s" % (data,1))
       

