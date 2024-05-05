from itertools import accumulate


def accumulate_2dim(H, W, M):
    """
    二次元累積和
    ゼータ変換、メビウス変換という
    かっこいい
    https://qiita.com/convexineq/items/afc84dfb9ee4ec4a67d5
    """

    # 縦方向の累積和
    for y in range(1, H):
        for x in range(W):
            M[y][x] += M[y - 1][x]

    # 横方向の累積和
    for y in range(H):
        for x in range(1, W):
            M[y][x] += M[y][x - 1]

    return M
