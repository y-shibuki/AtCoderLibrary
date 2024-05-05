"""
平衡二分探索木（SegmentTree）
init: O(N)
update(k, x): O(logN)
query(l, r): O(logN)
"""
class SegmentTree:
    def __init__(self, lst, func, initial_val):
        """
        lst: 対象の配列
        func: 区間に対して実行する関数。引数は2つ。
        initial_val: 初期値
        """
        n = len(lst)
        self.segfunc = func
        self.initial_val = initial_val
        self.num = 1 << (n - 1).bit_length()
        self.tree = [initial_val] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = lst[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """k番目の値をxに更新"""
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """区間[l, r)から該当する値を取得する。"""
        res = self.initial_val

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res