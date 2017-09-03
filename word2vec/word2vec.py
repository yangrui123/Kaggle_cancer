#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'


import math

import word_count as wc
from HuffmanTree import HuffmanTree
import numpy as np
import jieba
from sklearn import preprocessing


class Word2Vec():
    def __init__(self, vec_len=15000, learn_rate=0.025, win_len=5, model='cbow'):
        self.cutted_text_list = None
        self.vec_len = vec_len
        self.learn_rate = learn_rate
        self.win_len = win_len
        self.model = model
        self.word_dict = None  # each element is a dict, including: word,possibility,vector,huffmancode
        self.huffman = None    # the object of HuffmanTree

import tensorflow as tf
def tensor_word2vec(batch_size, vocabulary_size, embedding_size, num_sampled):
    # Placeholders for inputs
    train_inputs = tf.placeholder(tf.int32, shape=[batch_size])
    train_labels = tf.placeholder(tf.int32, shape=[batch_size, 1])
    # 参数
    embeddings = tf.Variable(tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0))
    embed = tf.nn.embedding_lookup(embeddings, train_inputs)
    # Construct the variables for the NCE loss
    nce_weights = tf.Variable(tf.truncated_normal([vocabulary_size, embedding_size],stddev=1.0 / math.sqrt(embedding_size)))
    nce_biases = tf.Variable(tf.zeros([vocabulary_size]))
    #设置损失函数和优化算法
    # Compute the NCE loss, using a sample of the negative labels each time.
    loss = tf.reduce_mean(tf.nn.nce_loss(nce_weights, nce_biases, embed, train_labels,
                       num_sampled, vocabulary_size))
    # We use the SGD optimizer.
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=1.0).minimize(loss)
    #迭代训练
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for inputs, labels in generate_batch(batch_size, num_skips, skip_window):
            feed_dict = {train_inputs: inputs, train_labels: labels}
            _, cur_loss = sess.run([optimizer, loss], feed_dict=feed_dict)
            print("loss:",cur_loss)


if __name__ == '__main__':
    text_list = wc.load_txt('../static/wufazhangda.txt')
    WC = wc.WordCounter(text_list)
    c = WC.count_res
    # print(c)
    print(sum(c.values()))
    ht = HuffmanTree(c)