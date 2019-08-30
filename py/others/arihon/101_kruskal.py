# ARC 076 D
# クラスカル法による最小全域木問題

# 辺をコストの小さい順に見ていき、閉路ができない(Union-Findで判定)場合は追加する

from heapq import heappush, heappop


class UnionFind(object):

    def __init__(self, N):
        self.tree = [i for i in range(N)]
        self.rank = [0] * (N + 1)

    def find(self, x):
        if self.tree[x] == x:
            return x
        else:
            self.tree[x] = self.find(self.tree[x])  # 経路圧縮
            return self.tree[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        # ランクを考慮しない場合はどちらが親になっても良い
        if self.rank[x] < self.rank[y]:
            self.tree[x] = y
        else:
            self.tree[y] = x

        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    def has_same_parent(self, x, y):
        return self.find(x) == self.find(y)


N = int(input())
V = list()
for i in range(N):
    x, y = map(int, input().split())
    V.append((i, x, y))

# 全ての辺の組み合わせを考えると O(N^2) で明らかに間に合わない
# グラフがx, yの格子のみなので、全ての頂点をx座標とy座標それぞれについてソートした列で隣接する2点の張る辺だけを考えれば良い
edges = list()
V.sort(key=lambda v: v[1])
for i in range(1, N):
    (src_i, src_x, src_y), (dst_i, dst_x, dst_y) = V[i - 1], V[i]
    heappush(edges, (abs(dst_x - src_x), src_i, dst_i))
V.sort(key=lambda v: v[2])
for i in range(1, N):
    (src_i, src_x, src_y), (dst_i, dst_x, dst_y) = V[i - 1], V[i]
    heappush(edges, (abs(dst_y - src_y), src_i, dst_i))

# Kruskal法の実装 結局ヒープソートが一番時間かかって O(NlogN) になる
# コストの小さい辺から順にUnion-Find木に加えていく
# すでに同じ親になっている = 両頂点とも全域木に含まれている 場合はスキップする
total_cost = 0
uf = UnionFind(N)
while len(edges) != 0:
    cost, src, dst = heappop(edges)
    if uf.find(src) != uf.find(dst):
        uf.unite(src, dst)
        total_cost += cost

print(total_cost)
