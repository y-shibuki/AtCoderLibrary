from typing import Dict


class Indirected_Graph:
    def __init__(self, n: int) -> None:
        """頂点数nの無向グラフを生成する

        Args:
            n (int): 頂点の個数
        Note:
            頂点V_i(1 <= i <= n)です
        """
        self.nodes: Dict[int, set] = {(i + 1): set() for i in range(n)}

    def add_edge(self, v1: int, v2: int) -> None:
        """2つの頂点間に辺を追加する

        Args:
            v1 (int): 頂点
            v2 (int): 頂点
        """
        self.nodes[v1].add(v2)
        self.nodes[v2].add(v1)

    def remove_edge(self, v1: int, v2: int) -> None:
        """頂点v1, v2間の辺を削除する

        Args:
            v1 (int): 頂点
            v2 (int): 頂点
        """
        self.nodes[v1].remove(v2)
        self.nodes[v2].remove(v1)

    def remove_edges(self, v: int) -> None:
        """頂点vからの辺を全て削除する

        Args:
            v (int): 頂点
        """
        self.nodes[v] = set()

    def __getitem__(self, i: int) -> set:
        return self.nodes[i]

    def __str__(self) -> str:
        return "\n".join([f"{idx}:{val}" for idx, val in self.nodes.items()])

    __repr__ = __str__
