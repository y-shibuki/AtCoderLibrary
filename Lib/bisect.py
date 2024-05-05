import bisect


def index(a: list[int], x: int) -> int:  # 探索したい数値のindexを探索
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError


def find_lt(a, x):  # 探索したい数値未満のうち最大の数値を探索
    "Find rightmost value less than x"
    i = bisect.bisect_left(a, x)
    if i:
        return a[i - 1]
    raise ValueError


def find_le(a, x):  # 探索したい数値以下のうち最大の数値を探索
    "Find rightmost value less than or equal to x"
    i = bisect.bisect_right(a, x)
    if i:
        return a[i - 1]
    raise ValueError


def find_gt(a, x):  # 探索したい数値を超えるもののうち最小の数値を探索
    "Find leftmost value greater than x"
    i = bisect.bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


def find_ge(a, x):  # 探索したい数値以上のうち最小の数値を探索
    "Find leftmost item greater than or equal to x"
    i = bisect.bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


a = [2, 3, 5, 7, 11, 13, 17, 19]

print(index(a, 11))
print(find_lt(a, 11))
print(find_le(a, 11))
print(find_gt(a, 11))
print(find_ge(a, 11))
