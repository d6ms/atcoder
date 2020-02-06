class UnionFind(object):

    def __init__(self, N):
        self.tree = [i for i in range(N)]
        self.rank = [0] * (N + 1)
        self.size = [1] * N  # 頂点iの属する連結成分の大きさ

    def find(self, x):
        if self.tree[x] == x:
            return x
        else:
            self.tree[x] = self.find(self.tree[x])  # 経路圧縮
            return self.tree[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        # ランクを考慮しない場合はどちらが親になっても良い
        if self.rank[x] < self.rank[y]:
            self.tree[x] = y
            self.size[y] += self.size[x]
        else:
            self.tree[y] = x
            self.size[x] += self.size[y]

        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    def has_same_parent(self, x, y):
        return self.find(x) == self.find(y)