def ext_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    ax + by = gcd(a, b) = dとなるようなx, yの組を1つ求める
    返り値：(x, y, d)
    """
    if b == 0:
        return 1, 0, a

    s, t, d = ext_gcd(b, a % b)
    return t, s - (a // b) * t, d


def modinv(a: int, m: int) -> int:
    """
    aの逆元を求める( 1 / a (mod m)の値を求める )
    ax≡1 (mod m)となるようなxを求める。すなわち、
    ax + my = 1となるようなxを求めればよく、これは拡張ユークリッドの互除法を用いれば良い。
    """

    x, _, _ = ext_gcd(a, m)
    return x % m
