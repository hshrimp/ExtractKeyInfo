**关键词抽取**

### 关键词抽取

# 使用TFIDF算法和TextRank算法抽取文本关键词

`text = '''（原标题：央视独家采访：陕西榆林产妇坠楼事件在场人员还原事情经过）
        央视新闻客户端11月24日消息，2017年8月31日晚，在陕西省榆林市第一医院绥德院区，产妇马茸茸在待产时，从医院五楼坠亡。事发后，医院方面表示，由于家属多次拒绝剖宫产，最终导致产妇难忍疼痛跳楼。但是产妇家属却声称，曾向医生多次提出剖宫产被拒绝。
        事情经过究竟如何，曾引起舆论纷纷，而随着时间的推移，更多的反思也留给了我们，只有解决了这起事件中暴露出的一些问题，比如患者的医疗选择权，人们对剖宫产和顺产的认识问题等，这样的悲剧才不会再次发生。央视记者找到了等待产妇的家属，主治医生，病区主任，以及当时的两位助产师，一位实习医生，希望通过他们的讲述，更准确地还原事情经过。
        产妇待产时坠亡，事件有何疑点。公安机关经过调查，排除他杀可能，初步认定马茸茸为跳楼自杀身亡。马茸茸为何会在医院待产期间跳楼身亡，这让所有人的目光都聚焦到了榆林第一医院，这家在当地人心目中数一数二的大医院。
        就这起事件来说，如何保障患者和家属的知情权，如何让患者和医生能够多一份实质化的沟通？这就需要与之相关的法律法规更加的细化、人性化并且充满温度。用这种温度来消除孕妇对未知的恐惧，来保障医患双方的权益，迎接新生儿平安健康地来到这个世界。'''

ext = Extract()
print(ext.extract_keyword_textrank(text, 10))
print(ext.extract_keyword_tfidf(text, 10))`


result：
the words in the graph count 100
[('产妇', 1.0), ('医院', 0.6820867066672601), ('事件', 0.5310214948008278), ('家属', 0.5228384297328734), ('剖宫产', 0.422973957736309), ('患者', 0.40729413034088413), ('温度', 0.3232938868713188), ('榆林', 0.30244244595457587), ('客户端', 0.2646661722177803), ('还原', 0.259057325365607)]
[('产妇', 0.40344754583955217), ('医院', 0.2625139440568656), ('待产', 0.25557696273582087), ('剖宫产', 0.24101156946268654), ('家属', 0.22943491204626867), ('坠亡', 0.17426185226282917), ('事件', 0.17003818608447763), ('跳楼', 0.15528612075373133), ('患者', 0.14211751271104478), ('榆林', 0.1332964828716418)]
