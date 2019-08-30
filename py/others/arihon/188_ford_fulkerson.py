# ABC 010 D
# フォード・ファルカーソン法による最大流問題/最小カット問題
# 何故かWAがいくつか出たけど、アルゴリズム部分の実装が問題なわけではなさそう


class Edge(object):

    def __init__(self, src, dst, cap):
        self.src = src
        self.dst = dst
        self.cap = cap
        self.rev = None

    def create_rev(self):
        """
        対応する残余グラフの辺を作成して返す。
        本来の辺と残余グラフの辺は相互に参照を持ち合うため、このメソッド以外から生成しないこと。
        """
        rev = Edge(self.dst, self.src, 0)
        self.rev = rev
        rev.rev = self
        return rev


class FordFulkerson:

    def __init__(self, N):
        self.N = N
        self.G = [list() for _ in range(N)]  # G[i]: 頂点iに接続している全ての有向辺のリスト

    def add_edge(self, src, dst, cap):
        forward = Edge(src, dst, cap)
        backward = forward.create_rev()
        self.G[src].append(forward)
        self.G[dst].append(backward)

    def flow(self, src, dst):
        max_flow = 0
        while True:
            self.used = [0] * self.N
            flow = self._dfs(src, dst)
            if flow == 0:  # f=0 が返るのは全てのパスを走査してこれ以上検討するパスがなくなったタイミング
                break
            max_flow += flow
        return max_flow

    def _dfs(self, v, t, f=float('inf')):
        """
        深さ優先でグラフを走査し、目的地に達するパスがあるか検索する。
        パスが存在すればその時の最大流を返し、存在しなければ0を返す。
        最大流量がFである時、高々F回のDFSをすることになるため、 O(F|E|) となる。

        :param v: 始点のインデックス
        :param t: 終点のインデックス
        :param f: 現在の再帰スタックにおける暫定の最大流
        """
        if v == t:
            return f
        used = self.used
        used[v] = 1
        for e in self.G[v]:
            if e.cap and not used[e.dst]:
                d = self._dfs(e.dst, t, min(f, e.cap))
                if d:
                    e.cap -= d
                    e.rev.cap += d
                    return d
        return 0


# 「友達関係を切る」と「ログインできなくする」の2操作があるのが面倒なので、
# 全てのマークしている頂点と辺を張る頂点Gを追加し、頂点0とGの最小カット問題として解けば、操作をまとめることができる。
# 最小カット・最大フロー定理を利用して、最大フローをFord-Fulkerson法で求めれば終わり。
N, G, E = map(int, input().split())
P = list(map(int, input().split()))

ff = FordFulkerson(N + 1)
for _ in range(E):
    a, b = map(int, input().split())
    ff.add_edge(a, b, 1)
for p in P:
    ff.add_edge(p, N, 1)
print(ff.flow(0, N))
