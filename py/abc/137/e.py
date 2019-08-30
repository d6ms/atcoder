from math import isinf


class Edge(object):

    def __init__(self, src, dst, cost):
        self.src = src
        self.dst = dst
        self.cost = cost


class BellmanFord(object):

    def __init__(self, v_len, edges, start):
        """
        隣接行列を使っていないので、有向グラフにのみ適用可能。
        ベルマンフォード法によって最短経路を求める。
        ダイクストラと違って負の数も扱えるが、O(|V||E|) なのでダイクストラより遅い。

        :param v_len: グラフのノード数 通常は|V|、1-indexedなグラフなら |V| + 1
        :param edges: 辺のリスト
        :param start: 始点 単一視点最短経路問題として解くので必要
        """
        self._dist = [float('inf') for _ in range(v_len)]  # 始点から各頂点までの最短距離
        self._prev = [float('inf') for _ in range(v_len)]  # 最短経路における，その頂点の前の頂点のIDを格納する

        self._solve(edges, start)
        self.d = dict()
        for e in edges:
            self.d[(e.src, e.dst)] = e.cost

    def _solve(self, edges, start):
        self._dist[start] = 0

        cnt = 0
        while True:  # 更新は高々 |V| - 1 回で終わる
            cnt += 1
            updated = False
            for e in edges:
                if self._dist[e.src] + e.cost < self._dist[e.dst]:
                    self._dist[e.dst] = self._dist[e.src] + e.cost
                    self._prev[e.dst] = e.src
                    if cnt >= len(self._dist):
                        self._dist[e.dst] = float('-inf')
                    updated = True
            if not updated:
                break

    def distance(self, goal):
        """
        負の閉路を含む場合は -inf を返す。
        """
        return self._dist[goal]

    def path(self, goal):
        """
        負の閉路を含む場合は計算が終わらない。
        """
        path = list()
        path.append(goal)
        cursor = goal

        while not isinf(self._prev[cursor]):
            path.append(self._prev[cursor])
            cursor = self._prev[cursor]

        return list(reversed(path))

    def score(self, goal):
        s = 0
        p = self.path(goal)
        for i in range(len(p) - 1):
            s += self.d[(p[i], p[i + 1])]
        return s


N, M, P = map(int, input().split())
edges = list()
for _ in range(M):
    A, B, C = map(int, input().split())
    e = Edge(A, B, P - C)
    edges.append(e)
bf = BellmanFord(N + 1, edges, 1)

if isinf(bf.distance(N)):
    print(-1)
else:
    print(-min(0, bf.score(N)))