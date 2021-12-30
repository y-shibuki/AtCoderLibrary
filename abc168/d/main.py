import biseccollections,copy,heapq,itertools,math,numpy,string
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

N, M = LI()
m_ = [LI() for _ in range(M)]

m = {x:set() for x in range(N)}

for x, y in m_:
    m[x - 1].add(y - 1)
    m[y - 1].add(x - 1)

q = collections.deque()
q.append([0, 0, 0])
d = [-1 for _ in range(N)]
ans = [-1 for _ in range(N)]

while q:
    k = q.popleft()
    if d[k[0]] != -1: continue
    d[k[0]] = k[1]
    ans[k[0]] = k[2] + 1
    for x in m[k[0]]:
        q.append([x, k[1] + 1, k[0]])

for x in ans:
    if x == -1:
        print("No")
        exit()
print("Yes")
for x in ans[1:]:
    print(x)