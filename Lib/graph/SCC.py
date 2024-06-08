# 強連結成分分解(SCC)を行うクラス
# 計算量はO(N + M)
# Nはノード数、Mはエッジ数
# 
# 入力:
# N: 頂点サイズ
# 使い方:
# scc = SCC(N)
# label, group = scc.solve()
# G0, GP = scc.construct()
# 
# 強連結成分の数: label
# 各ノードの強連結成分のラベル: group
# 新しいグラフ: G0
# 強連結成分内のノードリスト: GP

import sys

sys.setrecursionlimit(10 ** 6)

class SCC:
    def __init__(self, N):
        self.N = N  # ノード数
        self.G =  {i: [] for i in range(N)} # グラフ
        self.RG = {i: [] for i in range(N)}  # 逆グラフ
        self.order = []  # 仕分け順序を格納するリスト
        self.used = [False] * N  # 訪問済みノードを管理するリスト
        self.label = 0  # 強連結成分のラベル
        self.group = [-1] * N  # 各ノードの強連結成分のラベルを格納するリスト

    def add_edge(self, v, w):
        self.G[v].append(w)
        self.RG[w].append(v)

    def dfs(self, v):
        # 深さ優先探索を行い、訪問順序を記録する
        self.used[v] = True
        for neighbor in self.G[v]:
            if not self.used[neighbor]:
                self.dfs(neighbor)
        self.order.append(v)

    def rdfs(self, v):
        # 逆グラフ上で深さ優先探索を行い、強連結成分をマークする
        self.group[v] = self.label
        for neighbor in self.RG[v]:
            if self.group[neighbor] == -1:
                self.rdfs(neighbor)

    def solve(self):
        # 強連結成分を求める関数
        for i in range(self.N):
            if not self.used[i]:
                self.dfs(i)

        while self.order:
            node = self.order.pop()
            if self.group[node] == -1:
                self.rdfs(node)
                self.label += 1
        return self.label, self.group

    def construct(self):
        # 強連結成分を使って新しいグラフを構築する
        G0 = [set() for _ in range(self.label)]
        GP = [[] for _ in range(self.label)]
        for v in range(self.N):
            lbs = self.group[v]
            for w in self.G[v]:
                lbt = self.group[w]
                if lbs != lbt:
                    G0[lbs].add(lbt)
            GP[lbs].append(v)
        return G0, GP

"""
scc = SCC(N)
for i, j in edges:
    scc.add_edge(i, j)
label, group = scc.solve()
G0, GP = scc.construct()
print(GP)
"""