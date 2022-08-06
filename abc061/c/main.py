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
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
# 文字を一行読み込み
# string
def S(): return sys.stdin.readline().rstrip()
# 空白区切りの文字を一行読み込み
# list<string>
def LS(): return list(sys.stdin.readline().rstrip().split())

N, K = LI()

l = dict()

for i in range(N):
    a, b = LI()
    if a in l:
        l[a] += b
    else:
        l[a] = b

l = sorted(l.items(), reverse=True)

while True:
    x = l.pop()
    K -= x[1]
    if K <= 0:
        print(x[0])
        exit()