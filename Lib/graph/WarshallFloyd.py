# ワーシャルフロイド法
# O(V^3)で全点対最短経路を求める
# O(V^2)で更新する
# https://qiita.com/rp523/items/8fba3882c4a6ea203757

class WarshallFloyd:
    def __init__(self, N, INF=1<<60):
        self.N = N  # 頂点の数
        self.INF = INF
        self.dist = [[INF] * N for _ in range(N)]  # 各頂点間の距離を保持する2次元リスト

        # 各頂点から自分自身への距離は0
        for i in range(N):
            self.dist[i][i] = 0

        self.total_distance = None  # 全頂点間の最短距離の合計

    # 辺を追加する
    def add_edge(self, a, b, c):
        self.dist[a][b] = self.dist[b][a] = c

    # ワーシャルフロイド法で全頂点間の最短距離を求める
    def solve(self):
        for k in range(self.N):
            for i in range(self.N):
                for j in range(self.N):
                    if self.dist[i][k] != self.INF and self.dist[k][j] != self.INF:
                        self.dist[i][j] = min(self.dist[i][j], self.dist[i][k] + self.dist[k][j])

        self.total_distance = sum([sum(self.dist[i][i + 1:]) for i in range(self.N)])

    # 辺の情報を更新する
    def update_edge(self, a, b, c):
        # 既に最短経路が求まっている場合は更新しない
        if self.dist[a][b] <= c:
            return

        for i in range(self.N):
            for j in range(i + 1, self.N):
                temp_cost = min(self.dist[i][a] + c + self.dist[b][j], self.dist[i][b] + c + self.dist[a][j])

                if self.dist[i][j] > temp_cost:
                    self.total_distance -= self.dist[i][j] - temp_cost
                    self.dist[i][j] = self.dist[j][i] = temp_cost

    # 全頂点間の最短距離の合計を取得する
    def get_total_distance(self):
        return self.total_distance

"""
wh = WarshallFloyd(N)

for _ in range(M):
    A, B, C = i_map()
    wh.add_edge(A - 1, B - 1, C)

wh.solve()

K = i_input()
for _ in range(K):
    X, Y, Z = i_map()
    wh.update_edge(X - 1, Y - 1, Z)
    print(wh.get_total_distance())
"""
