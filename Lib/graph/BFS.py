"""BFSの基本フォーマット

BFS(Breadth-First Search)
計算量: O(V + E) PythonよりもPyPyの方が確実に速い
参考: https://algo-method.com/descriptions/114
"""
from queue import Queue

from Indirected_Graph import Indirected_Graph


def main() -> None:
    N: int = 10  # 頂点数
    g = Indirected_Graph(N)

    # ここでグラフの入力

    # 何手目にアクセスされたか
    # -1は未探索を表す
    dist = [-1] * (N + 1)
    q: Queue[int] = Queue()

    # スタート位置を初期化
    dist[0] = 0
    q.put(0)

    while not q.empty():
        v = q.get()

        for next_v in g[v]:
            if dist[next_v] != -1:
                continue
            dist[next_v] = dist[v] + 1
            q.put(next_v)
