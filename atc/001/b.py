# b Union Find


class UnionFind(object):

    def __init__(self, N):
        self.tree = [i for i in range(N)]
        self.rank = [0] * (N + 1)

    def find(self, x):
        if self.tree[x] == x:
            return x
        else:
            self.tree[x] = self.find(self.tree[x])
            return self.tree[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.tree[x] = y
        else:
            self.tree[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    def has_same_parent(self, x, y):
        return self.find(x) == self.find(y)


# P = 0で連結、P = 1で判定
# 連結されるたびにUnion-Find木にグルーピングしていく
def solve(N, Q, P_A_B):
    unionfind = UnionFind(N)
    for p, a, b in P_A_B:
        if p == 0:
            unionfind.unite(a, b)
        elif p == 1:
            connected = unionfind.has_same_parent(a, b)
            print('Yes' if connected else 'No')


N, Q = map(int, input().split())
P_A_B = [tuple(map(int, input().split())) for _ in range(Q)]
solve(N, Q, P_A_B)