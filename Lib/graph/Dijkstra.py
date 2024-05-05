"""ダイクストラアルゴリズムの基本フォーマット

Dijkstra(Dijkstra法)
計算量: O((V+E)log(V)) PythonとPyPyの違いが分からない
参考: https://qiita.com/gottie/items/3eedf21a039a50aa341d
諸注意:
ループは不具合の原因
"""

import heapq
import sys


def dijkstra(graph, start, goal):
    """
    Atcoder用にNodeは1,2,3...（自然数）
    graphは隣接リスト（[node, weight]が保持されている）
    """
    n = len(graph)
    visited = [False] * (n + 1)
    distance = [sys.maxsize] * (n + 1)
    distance[start] = 0
    pq = [(0, start)]

    while pq:
        _, u = heapq.heappop(pq)

        if u == goal:
            return distance[goal]

        visited[u] = True

        for v, weight in graph[u]:
            if not visited[v] and (new_distance := distance[u] + weight) < distance[v]:
                distance[v] = new_distance
                heapq.heappush(pq, (new_distance, v))

    return None
