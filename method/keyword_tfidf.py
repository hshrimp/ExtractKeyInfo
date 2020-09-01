#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/9/1 下午2:45
"""
from collections import defaultdict
from jieba import posseg as psg


class TfIdf:
    def __init__(self):
        self.unKnow_idf = 0
        self.word2idf = {}
        self.word2tf = defaultdict(float)

        self.tag = {'n', 'a', 'v'}
        self.get_idf('data/idf.txt')

    def get_idf(self, path):
        """
        获取jieba分词的idf.txt文件中词的idf
        :param path:
        :return:
        """
        with open(path, 'r')as f:
            for line in f.readlines():
                word, idf = line.strip().split(' ')
                self.word2idf[word] = float(idf)
        self.unKnow_idf = sum(self.word2idf.values()) / len(self.word2idf)

    def compute_tf(self, text):
        """
        计算当前文本的词的词频
        :param text:
        :return:
        """
        word2num = defaultdict(int)
        seg_list = psg.lcut(text)
        for pair in seg_list:
            if pair.flag[0] in self.tag and len(pair.word) > 1:
                word2num[pair.word] += 1
        count = sum(word2num.values())
        for k, v in word2num.items():
            self.word2tf[k] = v / count

    def extract_keyword(self, text, number):
        """
        计算tfidf
        :param text:
        :param number:
        :return:
        """
        self.compute_tf(text)
        word2tfidf = defaultdict(float)
        for word, tf in self.word2tf.items():
            idf = self.word2idf.get(word, self.unKnow_idf)
            word2tfidf[word] = tf * idf
        res = sorted(word2tfidf.items(), key=lambda x: x[1], reverse=True)
        return res[:number]
