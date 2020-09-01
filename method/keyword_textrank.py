#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/8/31 下午5:04
"""
from method.textrank import TextRank
from jieba import posseg as psg
from collections import defaultdict


class TextRankKeyWord:
    def __init__(self):
        """
        初始化，只取词性为名词，形容词，动词，窗口设置为5
        """
        self.tag = {'n', 'a', 'v'}
        self.span = 5

    def extract_keyword(self, text, number):
        """
        抽取关键词
        :param text: 输入文本
        :param number: 抽取的关键词数量
        :return: 返回重要成都排前number的关键词
        """
        graph = TextRank()
        occu2num = defaultdict(int)
        seg_list = psg.lcut(text)
        for i, pair in enumerate(seg_list):
            if pair.flag[0] in self.tag and len(pair.word) > 1:
                for j in range(i + 1, i + 1 + self.span):
                    if j >= len(seg_list):
                        break
                    if seg_list[j].flag[0] not in self.tag or len(seg_list[j].word) < 2:
                        continue
                    if (seg_list[j].word, pair.word) in occu2num:
                        occu2num[(seg_list[j].word, pair.word)] += 1
                    else:
                        occu2num[(pair.word, seg_list[j].word)] += 1
        for key, value in occu2num.items():
            graph.add_edge(key[0], value, key[1])
        node_rank = graph.build_rank()
        node_rank = sorted(node_rank.items(), key=lambda x: x[1], reverse=True)
        return node_rank[:number]
