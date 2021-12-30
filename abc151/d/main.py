import sys
from collections import deque
import copy

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

H, W = LI()
m = [[True if x == "." else False for x in S()] for _ in range(H)]

result = 0
for i in range(W):
    for j in range(H):
        if not m[j][i]: continue
        memo = copy.deepcopy(m)
        memo[j][i] = True
        q = deque([[i, j, 0]])
        while q:
            k = q.popleft()
            if not ((0 <= k[0] < W) and (0 <= k[1] < H)): continue
            if memo[k[1]][k[0]]:
                memo[k[1]][k[0]] = False
            else:
                continue
            result = max(result, k[2])
            q.append([k[0] + 1, k[1], k[2] + 1])
            q.append([k[0] - 1, k[1], k[2] + 1])
            q.append([k[0], k[1] + 1, k[2] + 1])
            q.append([k[0], k[1] - 1, k[2] + 1])

print(result)