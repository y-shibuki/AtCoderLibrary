import sys
from math import gcd


def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input() for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]

def lcm(a: int, b: int) -> int: return a * b // gcd(a, b)
def ceil(a: int, b: int) -> int: return (a + b - 1) // b
def floor(a: int, b: int) -> int: return a // b


sys.setrecursionlimit(10 ** 6)
INF = 1 << 60
MOD = 10 ** 9 + 7
