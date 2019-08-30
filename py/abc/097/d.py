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


N, M = map(int, input().split())
P = list(map(int, input().split()))

uf = UnionFind(N + 1)
for _ in range(M):
    x, y = map(int, input().split())
    uf.unite(x, y)

ans = 0
for i in range(1, N + 1):
    ans += uf.has_same_parent(i, P[i - 1])
print(ans)
