# UnionFindの利用とreverseの発想まではOKだがTLE


class UnionFind(object):

    def __init__(self, N):
        self._tree = [i for i in range(N)]
        self._rank = [0] * (N + 1)

    def find(self, x):
        if self._tree[x] == x:
            return x
        else:
            self._tree[x] = self.find(self._tree[x])
            return self._tree[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        # ランクを考慮しない場合はどちらが親になっても良い
        if self._rank[x] < self._rank[y]:
            self._tree[x] = y
        else:
            self._tree[y] = x

        if self._rank[x] == self._rank[y]:
            self._rank[x] += 1

    def has_same_parent(self, x, y):
        return self.find(x) == self.find(y)


N, M = map(int, input().split())
A_B = [tuple(map(int, input().split())) for _ in range(M)]


def calc_inconvenience(unionfind, N):
    inconvenience = 0
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if not unionfind.has_same_parent(i, j):
                inconvenience += 1
    return inconvenience


result = list()
unionfind = UnionFind(N + 1)
for a, b in reversed(A_B):
    result.append(calc_inconvenience(unionfind, N))
    unionfind.unite(a, b)
for r in reversed(result):
    print(r)


