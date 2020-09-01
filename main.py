#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/8/31 下午5:58
"""
from method.keyword_textrank import TextRankKeyWord
from method.keyword_tfidf import TfIdf


class Extract:
    def __init__(self):
        self.keyword_textrank = TextRankKeyWord()
        self.keyword_tfidf = TfIdf()

    def extract_keyword_textrank(self, text, number):
        """
        使用textrank抽取关键词
        :param text:
        :param number:
        :return:
        """
        return self.keyword_textrank.extract_keyword(text, number)

    def extract_keyword_tfidf(self, text, number):
        """
        使用tfidf抽取关键词
        :param text:
        :param number:
        :return:
        """
        return self.keyword_tfidf.extract_keyword(text, number)


if __name__ == '__main__':
    text = '''（原标题：央视独家采访：陕西榆林产妇坠楼事件在场人员还原事情经过）
        央视新闻客户端11月24日消息，2017年8月31日晚，在陕西省榆林市第一医院绥德院区，产妇马茸茸在待产时，从医院五楼坠亡。事发后，医院方面表示，由于家属多次拒绝剖宫产，最终导致产妇难忍疼痛跳楼。但是产妇家属却声称，曾向医生多次提出剖宫产被拒绝。
        事情经过究竟如何，曾引起舆论纷纷，而随着时间的推移，更多的反思也留给了我们，只有解决了这起事件中暴露出的一些问题，比如患者的医疗选择权，人们对剖宫产和顺产的认识问题等，这样的悲剧才不会再次发生。央视记者找到了等待产妇的家属，主治医生，病区主任，以及当时的两位助产师，一位实习医生，希望通过他们的讲述，更准确地还原事情经过。
        产妇待产时坠亡，事件有何疑点。公安机关经过调查，排除他杀可能，初步认定马茸茸为跳楼自杀身亡。马茸茸为何会在医院待产期间跳楼身亡，这让所有人的目光都聚焦到了榆林第一医院，这家在当地人心目中数一数二的大医院。
        就这起事件来说，如何保障患者和家属的知情权，如何让患者和医生能够多一份实质化的沟通？这就需要与之相关的法律法规更加的细化、人性化并且充满温度。用这种温度来消除孕妇对未知的恐惧，来保障医患双方的权益，迎接新生儿平安健康地来到这个世界。'''

    ext = Extract()
    print(ext.extract_keyword_textrank(text, 10))
    print(ext.extract_keyword_tfidf(text, 10))
