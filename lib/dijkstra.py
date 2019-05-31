from typing import List
from heapq import heappush, heappop
from math import isinf


class Edge(object):

    def __init__(self, src: int, dst: int, cost: int):
        self.src = src
        self.dst = dst
        self.cost = cost


class Dijkstra(object):

    def __init__(self, v_len: int, edges: List[Edge], start: int, directed=False):
        """
        ダイクストラ法で最短経路を求める。

        :param v_len: グラフのノード数 通常は|V|、1-indexedなグラフなら |V| + 1
        :param edges: グラフの構造
        :param start: 始点 単一視点最短経路問題として解くので必要
        :param directed: 有向グラフの場合True 隣接行列を対称行列にするかが変わる
        """

        # 隣接行列 (adjacency matrix)
        # adj[i][j] でi番目の頂点からj番目の頂点へのコストを示す パスがなければINF
        self._adj = [[float('inf') for _ in range(v_len)] for _ in range(v_len)]
        for e in edges:
            self._adj[e.src][e.dst] = e.cost
            if not directed:
                self._adj[e.dst][e.src] = e.cost
        self._dist = [float('inf') for i in range(v_len)]  # 始点から各頂点までの最短距離
        self._prev = [float('inf') for i in range(v_len)]  # 最短経路における，その頂点の前の頂点のIDを格納する

        self._solve(start)

    def _solve(self, start: int):
        # 「最短距離が確定した頂点」に隣接する点からBFSするにあたり、それをどう探すかが問題になる
        # 安直に実装すればここで O(|V|) かかってしまうが、優先度キューを使えば O(log|V|) になる
        self._dist[start] = 0
        q = list()
        heappush(q, (0, start))  # キューの要素は (始点から頂点v_iへの仮の距離, v_iのID)

        while len(q) != 0:
            c, src = heappop(q)
            if self._dist[src] < c:
                continue

            # 隣接行列から隣接するノードを全て調べる = BFS
            for dst in range(len(self._adj)):
                cost = self._adj[src][dst]
                if isinf(cost):
                    continue
                if self._dist[src] + cost < self._dist[dst]:
                    self._dist[dst] = self._dist[src] + cost
                    heappush(q, (self._dist[dst], dst))
                    self._prev[dst] = src

    def distance(self, goal: int):
        return self._dist[goal]

    def path(self, goal: int):
        path = list()
        path.append(goal)
        cursor = goal

        while not isinf(self._prev[cursor]):
            path.append(self._prev[cursor])
            cursor = self._prev[cursor]

        return list(reversed(path))
