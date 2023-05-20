# エラトステネスの篩
# 参考：https://zenn.dev/noodlewhale/articles/c5b069237ee72a
# https://ja.wikipedia.org/wiki/エラトステネスの篩
def get_prime(n: int):
    primes = []

    if n <= 1:  return []

    is_prime = [False, False] + [True] * (n - 1)

    for p in range(2, n + 1):
        if not is_prime[p]: continue
        primes.append(p)
        for i in range(p * p, n + 1, p):
            is_prime[i] = False

    return primes

# 素因数分解
# [素数, 指数]の二次元配列を返す関数
def prime_factorize(n: int):
    res = []

    for p in range(2, int(n ** 0.5) + 1):
        if n % p != 0: continue
        ex = 0
        while n % p == 0:
            ex += 1
            n //= p
        res.append([p, ex])
    if n != 1:
        res.append([n, 1])

    return res