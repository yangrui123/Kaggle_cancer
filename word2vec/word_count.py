#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'

import jieba
import pickle
from collections import Counter
from operator import itemgetter


def load_pickle(path):  # 读入pickle文件，不做任何变动
    file = open(path, 'rb')
    data = pickle.load(file)
    file.close()
    return data


def load_txt(path):
    fp = open(path, 'r', encoding='UTF-8')
    lines = fp.readlines()
    #data = [line.strip() for line in lines]
    return lines


class WordCounter():
    def __init__(self, text_list):
        self.text_list = text_list
        self.stop_words = self.Get_Stop_Words()
        self.count_res = None
        self.Word_Count(self.text_list)

    def Get_Stop_Words(self):
        # 获取停用词
        ret = load_pickle('../static/stop_words.pkl')
        return ret

    def Word_Count(self, text_list, cut_all=False):
        filtered_word_list = []
        count = 0
        for line in text_list:
            res = jieba.cut(line, cut_all=cut_all)
            res = list(res)
            text_list[count] = res
            count += 1
            filtered_word_list.extend(res)

        self.count_res = MulCounter(filtered_word_list)
        for word in self.stop_words:
            try:
                self.count_res.pop(word)
            except:
                pass


class MulCounter(Counter):
    def __init__(self, element_list):
        super().__init__(element_list)
        #print(self.larger_than(3))

    def larger_than(self, minvalue, ret='list'):
        # 过滤掉低频词汇
        temp = sorted(self.items(), key=itemgetter(1), reverse=True)
        low = 0
        high = temp.__len__()
        while (high - low > 1):
            mid = (low + high) >> 1
            if temp[mid][1] >= minvalue:
                low = mid
            else:
                high = mid
        if temp[low][1] < minvalue:
            if ret == 'dict':
                return {}
            else:
                return []
        if ret == 'dict':
            ret_data = {}
            for ele, count in temp[:high]:
                ret_data[ele] = count
            return ret_data
        else:
            return temp[:high]

    def less_than(self, maxvalue, ret='list'):
        # 去掉高频词汇
        temp = sorted(self.items(), key=itemgetter(1))
        low = 0
        high = temp.__len__()
        while ((high - low) > 1):
            mid = (low + high) >> 1
            if temp[mid][1] <= maxvalue:
                low = mid
            else:
                high = mid
        if temp[low][1] > maxvalue:
            if ret == 'dict':
                return {}
            else:
                return []
        if ret == 'dict':
            ret_data = {}
            for ele, count in temp[:high]:
                ret_data[ele] = count
            return ret_data
        else:
            return temp[:high]


if __name__ == '__main__':
    text_list = load_txt('../static/wufazhangda.txt')
    WC = WordCounter(text_list)
    c = WC.count_res
    #print(c)
    print(sum(c.values()))
