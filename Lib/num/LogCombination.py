# LogCombinationクラス: 組み合わせ(nCr)、順列(nPr)、階乗(n!)の常用対数を求める
# Logを用いることで、桁数が大きくなっても計算が容易になる
# log_combination(5, 2) = 0.99999...となるように精度は劣るが、2値比較などで使える


class LogCombination():
    def __init__(self, max_value):
        from itertools import accumulate
        from math import log10

        self.log_table = [0] + [log10(i) for i in range(1, max_value + 1)]
        self.acc_log_table = list(accumulate(self.log_table))

    # 組み合わせ(nCr)の常用対数を求める
    def log_combination(self, n, r):
        return self.acc_log_table[n] - self.acc_log_table[r] - self.acc_log_table[n - r]

    # 順列(nPr)を求める
    def log_permutation(self, n, r):
        return self.acc_log_table[n] - self.acc_log_table[n - r]

    # 重複順列(nHk)を求める
    # n種類のものから重複を許してk個選ぶ場合の数
    def log_duplication(self, n, k):
        return self.log_combination(n + k - 1, k)

    # 階乗(n!)を求める
    def log_factorial(self, n):
        return self.acc_log_table[n]