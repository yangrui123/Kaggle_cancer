#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'


fp = open("C:\\Users\m1833\Desktop\\training_text", 'r', encoding='UTF-8')
lines = fp.readlines()
fp.close()
fp = open("C:\\Users\m1833\Desktop\\training_variants", 'r', encoding='UTF-8')
lines2 = fp.readlines()
fp.close()
fwp = open("C:\\Users\m1833\Desktop\\training.txt", 'w', encoding='UTF-8')
fwp.write('\t'.join(['ID', 'Gene', 'Variation', 'Class', 'Text']))
fwp.write('\n')
var_dict = {}
for line in lines2[1:]:
    line_list = line.strip('\n').split(',')
    ID, gene, variation, Class = line_list[0], line_list[1], line_list[2], line_list[3]
    var_dict[ID] = [gene, variation, Class]
for line in lines[1:]:
    line_list = line.strip('\n').split('||')
    text = '"'+line_list[1]+'"'
    ID = line_list[0]
    tmp_list = [ID]+var_dict[ID] + [text]
    fwp.write('\t'.join(tmp_list))
    fwp.write('\n')
fwp.close()