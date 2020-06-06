import sys
sys.setrecursionlimit(300000)
from collections import deque

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


class SegmentTree(object):

    def __init__(self, A, e, fn):  # O(N)
        """
        :param A: 区間クエリの対象となる配列
        :param e: 単位元 fn(a, e) = fn(e, a) = a
        :param fn: (a, b) -> x な関数 a, bは交換則を満たす
        """
        self.e = e
        self.fn = fn
        self.length = 2 ** (len(A) - 1).bit_length()
        self.tree = [e] * 2 * self.length
        for i in range(len(A)):
            self.tree[i + self.length - 1] = A[i]
        for i in reversed(range(self.length - 1)):
            self.tree[i] = self.fn(self.tree[2 * i + 1], self.tree[2 * i + 2])

    def at(self, i):
        return self.tree[i + self.length - 1]

    # 配列のi番目をxに更新する
    def update(self, i, x):  # O(logN)
        i += self.length - 1
        self.tree[i] = x
        while i:
            i = (i - 1) // 2
            self.tree[i] = self.fn(self.tree[i * 2 + 1], self.tree[i * 2 + 2])

    # 区間[p, q)に関するクエリに答える
    def query(self, p, q):  # O(logN)
        if q <= p:
            return self.e
        p += self.length - 1
        q += self.length - 2
        res = self.e
        while q - p > 1:
            if p & 1 == 0:
                res = self.fn(res, self.tree[p])
            if q & 1 == 1:
                res = self.fn(res, self.tree[q])
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = self.fn(res, self.tree[p])
        else:
            res = self.fn(self.fn(res, self.tree[p]), self.tree[q])
        return res


N = I()
val2Idx = dict()
col1 = [0] * N
col2 = [0] * N
stock = list()
for i in range(N):
    _, *T = MI()
    for t in T:
        val2Idx[t] = i
    T = deque(T)
    col1[i] = T.popleft()
    if len(T) > 0:
        col2[i] = T.popleft()
    stock.append(T)
M = I()
A = LMI()

s1 = SegmentTree(col1, 0, max)
s2 = SegmentTree(col2, 0, max)
for a in A:
    ans = s1.query(0, N)
    if a == 1:
        print(ans)
        i = val2Idx[ans]
        s1.update(i, s2.at(i))
        s2.update(i, stock[i].popleft() if len(stock[i]) > 0 else 0)
    else:
        ans2 = s2.query(0, N)
        if ans > ans2:
            print(ans)
            i = val2Idx[ans]
            s1.update(i, s2.at(i))
            s2.update(i, stock[i].popleft() if len(stock[i]) > 0 else 0)
        else:
            print(ans2)
            i = val2Idx[ans2]
            s2.update(i, stock[i].popleft() if len(stock[i]) > 0 else 0)
