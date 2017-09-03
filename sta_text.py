#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'

import re
import matplotlib
import nltk
import json

filename = "C:\\Users\m1833\Desktop\\training.txt"

fp = open(filename,'r',encoding='UTF-8')
lines = fp.readlines()
fp.close()
class_dict = {}
lsents = []
fwp = open("text.txt", 'w', encoding='utf-8')
sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
for line in lines[1:]:
    line_list = line.strip('\n').split('\t')
    ID, gene, variation, Class, text = line_list[0], line_list[1], line_list[2], line_list[3], line_list[4]
    sents = sent_tokenizer.tokenize(text)
    cleanLine = [re.split(u'[!"#$%&()\*+,./:;<=>?@[\]^_`{|}~ ]', sent) for sent in sents]  # 去掉ASCII 标点符号
    for sent in cleanLine:
        sent = [word for word in sent if word!='']
        fwp.write('_'.join(sent))
        fwp.write('\t')
        fwp.write(Class)
        fwp.write('\n')
        lsents.append(len(sent))
fwp.close()
