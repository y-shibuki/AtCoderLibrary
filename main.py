import sys
from math import gcd
from typing import List

# 重複順列はproduct


def i_input() -> int: return int(input())
def i_map() -> map[int]: return map(int, input().split())
def i_list() -> List[int]: return list(i_map())
def i_row(N: int) -> List[int]: return [i_input() for _ in range(N)]
def i_row_list(N: int) -> List[List[int]]: return [i_list() for _ in range(N)]
def s_input() -> str: return input()
def s_map() -> List[str]: return input().split()
def s_list() -> List[str]: return list(s_map())
def s_row(N: int) -> List[str]: return [s_input() for _ in range(N)]
def s_row_str(N: int) -> List[List[str]]: return [s_list() for _ in range(N)]
def s_row_list(N: int) -> List[List[str]]: return [list(s_input()) for _ in range(N)]
def lcm(a: int, b: int) -> int: return a * b // gcd(a, b)
# math.ceil, floorはある程度大きな値で誤差が生じるらしい
def ceil(a: int, b: int) -> int: return (a + b - 1) // b
def floor(a: int, b: int) -> int: return a // b
# MODの逆元
def modinv(a: int) -> int: return pow(a, MOD-2, MOD)


sys.setrecursionlimit(10 ** 6)
INF = float('inf')
MOD = 10 ** 9 + 7


def main() -> None:
    pass


if __name__ == '__main__':
    main()
