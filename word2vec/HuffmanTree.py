#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'


import numpy as np


class HuffmanTreeNode():
    def __init__(self,value,possibility):
        # common part of leaf node and tree node
        self.possibility = possibility
        self.left = None
        self.right = None
        # value of leaf node  will be the word, and be
        # mid vector in tree node
        self.value = value # the value of word
        self.Huffman = "" # store the huffman code

    def __str__(self):
        return 'HuffmanTreeNode object, value: {v}, possibility: {p}, Huffman: {h}'\
            .format(v=self.value,p=self.possibility,h=self.Huffman)


class HuffmanTree():
    def __init__(self, word_dict, vec_len=15000):
        self.vec_len = vec_len      # the length of word vector
        self.root = None
        word_dict_list = list(word_dict.values())
        node_list = [HuffmanTreeNode(x['word'],x['possibility']) for x in word_dict_list]
        self.build_tree(node_list)
        # self.build_CBT(node_list)
        self.generate_huffman_code(self.root, word_dict)

    def build_tree(self,node_list):
        # node_list.sort(key=lambda x:x.possibility,reverse=True)
        # for i in range(node_list.__len__()-1)[::-1]:
        #     top_node = self.merge(node_list[i],node_list[i+1])
        #     node_list.insert(i,top_node)
        # self.root = node_list[0]

        while node_list.__len__()>1:
            i1 = 0  # i1表示概率最小的节点
            i2 = 1  # i2 概率第二小的节点
            if node_list[i2].possibility < node_list[i1].possibility :
                [i1,i2] = [i2,i1]
            for i in range(2,node_list.__len__()): # 找到最小的两个节点
                if node_list[i].possibility<node_list[i2].possibility :
                    i2 = i
                    if node_list[i2].possibility < node_list[i1].possibility :
                        [i1,i2] = [i2,i1]
            top_node = self.merge(node_list[i1],node_list[i2])
            if i1<i2:
                node_list.pop(i2)
                node_list.pop(i1)
            elif i1>i2:
                node_list.pop(i1)
                node_list.pop(i2)
            else:
                raise RuntimeError('i1 should not be equal to i2')
            node_list.insert(0,top_node)
        self.root = node_list[0]


if __name__ == '__main__':
    ht = HuffmanTree()