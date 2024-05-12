"""BFSの基本フォーマット

BFS(Breadth-First Search)
計算量: O(V + E) PythonよりもPyPyの方が確実に速い
参考: https://algo-method.com/descriptions/114
"""
from collections import deque

from Indirected_Graph import Indirected_Graph


def main() -> None:
    N: int = 10  # 頂点数
    g = Indirected_Graph(N)

    # ここでグラフの入力

    # 何手目にアクセスされたか
    # -1は未探索を表す
    dist = [-1] * (N + 1)
    q: Queue[int] = Queue()

    # スタート位置を初期化
    dist[1] = 1
    q.put(1)

    while not q.empty():
        v = q.get()

        for next_v in g[v]:
            if dist[next_v] != -1:
                continue
            dist[next_v] = dist[v] + 1
            q.put(next_v)


def bfs(M: dict[int, list[int]], S: int):
    from collections import deque

    N = len(M)

    # 何手目にアクセスされたか
    # -1は未探索を表す
    dist = [-1] * (N + 1)
    q = deque()

    # スタート位置を初期化
    dist[S] = 1
    q.append(S)

    while q:
        v = q.popleft()

        for next_v in M[v]:
            if dist[next_v] != -1:
                continue
            dist[next_v] = dist[v] + 1
            q.append(next_v)



INF = float('inf')


def bfs_2d(M: list[list[Any]], sx: int, sy: int) -> list[list[int]]:
    from collections import deque

    H = len(M)
    W = len(M[0])
    dist = [[INF] * W for _ in range(H)]
    q = deque()

    dist[sy][sx] = 0
    q.append((sx, sy))

    while len(q):
        x, y = q.popleft()
        for ax, ay in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            try:
                if M[y + ay][x + ax] == "#" or dist[y + ay][x + ax] <= dist[y][x] + 1:
                    continue

                dist[y + ay][x + ax] = dist[y][x] + 1
                q.append((x + ax, y + ay))
            except IndexError:
                continue


def bfs(p) -> int:
    q = deque([p])
    route = {p}
    invalid_start.add(p)

    while q:
        x, y = q.popleft()
        for ax, ay in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = (x + ax, y + ay)
            if 0 <= nx < W and 0 <= ny < H and S[ny][nx] != "#" and (nx, ny) not in invalid_start:
                route.add((nx, ny))
                if S[ny][nx] == ".":
                    invalid_start.add((nx, ny))
                    q.append((nx, ny))

    return len(route)