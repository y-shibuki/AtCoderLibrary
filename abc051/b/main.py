import sys

"""
よく使う関数
bisect
    bisect()
collections
    deque()
    Counter()
    most_common()
    defaultdict()
copy
    deepcopy()
    heapq
    heapify()
    heappush()
    heappop()
    itertools
    accumulate()
    groupby()
    product()重複あり
    permutations()重複なし(順列)
    combinations()重複なし(組み合わせ)
math
    gcd()
    ceil()
    factorial()
numpy
    fmax()
    argmax()
    vstack()
string
    ascii_lowercase()
    ascii_uppercase()
    lower()
    upper()
    swapcase()
"""

# 整数を一行のみ読み込み
# int


def I(): return int(sys.stdin.readline().rstrip())
# 空白区切りの整数を一行読み込み
# list<int>
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
# 文字を一行読み込み
# string
def S(): return sys.stdin.readline().rstrip()
# 空白区切りの文字を一行読み込み
# list<string>
def LS(): return list(sys.stdin.readline().rstrip().split())


K, S = LI()

result = 0
for x in range(K + 1):
    for y in range(max(x, S - K - x), min(K, (S - x) // 2) + 1):
        z = S - x - y
        if x == y:
            if y == z:
                result += 1
            else:
                result += 3
        elif y == z:
            result += 3
        else:
            result += 6

print(result)
