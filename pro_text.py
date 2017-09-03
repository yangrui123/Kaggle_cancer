#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'

"""
英文的词干化和去停用词
"""

import re
from nltk.corpus import stopwords
import collections
cachedStopWords = stopwords.words("english")

filename = "C:\\Users\m1833\Desktop\\training.txt"

fp = open(filename,'r',encoding='UTF-8')
lines = fp.readlines()
fp.close()
class_dict = {}
length_sents = []
for line in lines[1:len(lines)-100]:
    line_list = line.strip('\n').split('\t')
    ID, gene, variation, Class, text = line_list[0], line_list[1], line_list[2], line_list[3], line_list[4]
    text = ''.join(re.split(r'[\n,\r\n]', text))
    words = re.split(u'[(),.!?; "]', text)
    fwords = [word.lower() for word in words if word!='']
    wordsNum = collections.Counter(word for word in fwords)
    sort_words = [item[0] for item in wordsNum.most_common(5)]
    if Class not in class_dict.keys():
        class_dict[Class] = []
    class_dict[Class].extend(sort_words)

print(class_dict['2'])
print(class_dict['3'])
# fwp = open('key_words.txt', 'w', encoding='utf-8')
# for key in class_dict.keys():
#     words = set(class_dict[key])
#     words = ','.join(list(words))
#     fwp.write('\t'.join([key, words]))
#     fwp.write('\n')
# fwp.close()
#
# fwp = open('test.txt', 'w', encoding='utf-8')
# for line in lines[len(lines)-100:]:
#     line_list = line.strip('\n').split('\t')
#     ID, gene, variation, Class, text = line_list[0], line_list[1], line_list[2], line_list[3], line_list[4]
#     text = ''.join(re.split(r'[\n,\r\n]', text))
#     words = re.split(u'[,.!?; "]', text)
#     words = [word for word in words if word not in cachedStopWords]
#     wordsNum = collections.Counter(word.lower() for word in words)
#     sort_words = [item[0] for item in wordsNum.most_common(3)]
#     fwp.write('\t'.join([ID, Class, ','.join(sort_words)]))
#     fwp.write('\n')
# fwp.close()
#








