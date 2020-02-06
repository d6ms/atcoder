class UnionFind(object):

    def __init__(self, N):
        self._tree = [i for i in range(N)]
        self._rank = [0] * (N + 1)
        self.size = [1] * N
        self.inconvenience = N * (N - 1) // 2

    def find(self, x):
        if self._tree[x] == x:
            return x
        else:
            self._tree[x] = self.find(self._tree[x])
            return self._tree[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        self.inconvenience -= self.size[x] * self.size[y]
        if self._rank[x] < self._rank[y]:
            self._tree[x] = y
            self.size[y] += self.size[x]
        else:
            self._tree[y] = x
            self.size[x] += self.size[y]

        if self._rank[x] == self._rank[y]:
            self._rank[x] += 1


N, M = map(int, input().split())
A_B = [tuple(map(int, input().split())) for _ in range(M)]

result = list()
uf = UnionFind(N)
for a, b in reversed(A_B):
    result.append(max(0, uf.inconvenience))
    uf.unite(a - 1, b - 1)
for r in reversed(result):
    print(r)
