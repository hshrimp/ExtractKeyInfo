#!/usr/bin/env python
# encoding: utf-8
"""
@author: wushaohong
@time: 2020/8/31 下午4:15
"""
from collections import defaultdict


class TextRank:
    def __init__(self):
        self.graph = defaultdict(list)
        # 阻尼系数
        self.d = 0.85
        # eta值，迭代误差小于该值时跳出迭代
        self.eta = 1e-5

    def add_edge(self, start, weight, end):
        """
        生成初始图
        :param start: 起始点
        :param weight: 边的权重
        :param end: 结束点
        :return:
        """
        self.graph[start].append((start, weight, end))
        self.graph[end].append((end, weight, start))

    def build_rank(self):
        """
        迭代排序，起始点的权重s = (1-d)+d*sum(与起始点连接的每条边的权重/结束点所有边的权重和*结束点的权重)
        :return:
        """
        print(f'the words in the graph count {len(self.graph)}')
        node_weight = 1 / (len(self.graph) or 1)
        node2weight = defaultdict(float)
        out_sum = defaultdict(float)
        for node, edge_list in self.graph.items():
            node2weight[node] = node_weight
            out_sum[node] = sum([w[1] for w in edge_list])
        step_val = [0]
        for step in range(1, 1000):
            for node in self.graph.keys():
                s = 0
                for edge in self.graph[node]:
                    s += edge[1] / out_sum[edge[2]] * node2weight[edge[2]]
                node2weight[node] = (1 - self.d) + self.d * s
            step_val.append(sum(node2weight.values()))
            if abs(step_val[step] - step_val[step - 1]) <= self.eta:
                break

        # 归一化
        max_weight = max(node2weight.values())
        min_weight = min(node2weight.values())
        for node in node2weight.keys():
            node2weight[node] = (node2weight[node] - min_weight) / (max_weight - min_weight)

        return node2weight
