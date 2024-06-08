# Combinationクラス: 組み合わせ(nCr)、順列(nPr)、階乗(n!)を求める

MOD = 10**9 + 7

class Combination():
    def __init__(self, max_value):
        self.factorial_table = [1, 1] + [None] * (max_value - 1)
        self.inverse_table = [1, 1] + [None] * (max_value - 1)
        self.inverse_calc_table = [0, 1] + [None] * (max_value - 1)
        # テーブルの初期化
        for i in range(2, max_value + 1):
            self.factorial_table[i] = self.factorial_table[i - 1] * i % MOD
            self.inverse_calc_table[i] = -self.inverse_calc_table[MOD % i] * (MOD // i) % MOD
            self.inverse_table[i] = self.inverse_table[i - 1] * self.inverse_calc_table[i] % MOD

    # 組み合わせ(nCr)を求める
    def combination(self, n, r):
        return self.factorial_table[n] * self.inverse_table[r] * self.inverse_table[n - r] % MOD

    # 順列(nPr)を求める
    def permutation(self, n, r):
        return self.factorial_table[n] * self.inverse_table[n - r] % MOD

    # 重複順列(nHk)を求める
    # n種類のものから重複を許してk個選ぶ場合の数
    def duplication(self, n, k):
        return self.combination(n + k - 1, k)

    # 階乗(n!)を求める
    def factorial(self, n):
        return self.factorial_table[n]