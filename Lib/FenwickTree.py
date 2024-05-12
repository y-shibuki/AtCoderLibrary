"""
フェニック木（FenwickTree）
add(p, x): O(logN)
sum(l, r): O(logN)
"""
class FenwickTree:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n
    
    def add(self, p, x):
        p += 1  # 1-indexに調整
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p
    
    def sum(self, l, r):
        return self._sum(r) - self._sum(l)
    
    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s
