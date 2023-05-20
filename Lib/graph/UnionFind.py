# Union-Find
# 参考：https://atcoder.jp/contests/abc292/submissions/39416571
# 　　　https://algo-method.com/descriptions/133
# 　　　https://algo-method.com/descriptions/132
# n => 頂点の個数
# parent => 要素xの親頂点の番号、自身が根の場合は、(-集合の頂点数)
# groups => 集合の数
class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n
        self.parent = [-1] * n
        self.groups = n

    def find(self, x: int) -> int:
        """要素xが属する集合を求める

        Args:
            x (int): 要素x

        Returns:
            int: 要素xが属する集合の根
        """
        if self.parent[x] < 0:
            return x
        p = x
        while self.parent[p] >= 0:
            p = self.parent[p]
        # 経路圧縮
        while self.parent[x] >= 0:
            self.parent[x], x = p, self.parent[x]
        return p

    def union(self, x: int, y: int) -> bool:
        """集合XとYを併合する

        Args:
            x (int): 集合Xに属する要素x
            y (int): 集合Yに属する要素y

        Returns:
            bool: すでに併合済みならFalse、そうでないならTrue
        """
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.parent[x] > self.parent[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        self.groups -= 1
        return True

    def size(self, x: int) -> int:
        return -self.parent[self.find(x)]

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def members(self, x: int) -> list:
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self) -> list:
        return [i for i, x in enumerate(self.parent) if x < 0]

    def group_count(self) -> int:
        return self.groups

    def sizes(self) -> dict:
        return {i: -x for i, x in enumerate(self.parent) if x < 0}

    def all_group_members(self) -> dict:
        from collections import defaultdict

        d = defaultdict(list)
        for i in range(self.n):
            p = self.find(i)
            d[p].append(i)
        return d

    def __str__(self) -> str:
        return "\n".join(
            "{}: {}".format(k, v) for k, v in self.all_group_members().items()
        )

    __repr__ = __str__
