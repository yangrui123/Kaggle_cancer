#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'

import sklearn
fp = open('key_words.txt', 'r', encoding='utf-8')
lines = fp.readlines()
fp.close()
class_dict = {}
for line in lines:
    line_list = line.strip('\n').split('\t')
    Class = line_list[0]
    words = line_list[1].split(',')
    class_dict[Class] = words
fp = open('test.txt', 'r', encoding='utf-8')
lines = fp.readlines()
fp.close()
class_list = []
res = 0
for line in lines:
    line_list = line.strip('\n').split('\t')
    ID, Class, words = line_list[0], line_list[1], line_list[2].split(',')
    score_list = []
    for key in ['1','2','3','4','5','6','7','8','9']:
        words_list = class_dict[key]
        score = 0
        for word in words:
            if word in words_list:
                score += 1
        score_list.append(score)
    label = score_list.index(max(score_list))+1
    print(Class,label)
    sklearn.metrics(int(Class),int(label))
    if label == Class:
        res += 1
print(res/len(lines))



