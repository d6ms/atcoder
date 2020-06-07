# 要素updateと区間クエリ
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

    # 現在のi番目の要素を取得する
    def at(self, i):  # O(1)
        return self.tree[i + self.length - 1]


# 区間updateと要素クエリ
class SegmentTree(object):

    def __init__(self, A, e, fn):
        self.fn = fn
        self.length = 2 ** (len(A) - 1).bit_length()
        self.data = [e] * (self.length * 2)
        for i in range(len(A)):
            self.data[i + self.length - 1] = A[i]
        for i in reversed(range(self.length - 1)):
            self.data[i] = self.fn(self.data[2 * i + 1], self.data[2 * i + 2])

    # 区間[l, r)の値とxをfnで比較して更新する
    def update(self, l, r, x):  # O(logN)
        l += self.length
        r += self.length
        while l < r:
            if l & 1:
                self.data[l] = self.fn(self.data[l], x)
                l += 1
            if r & 1:
                self.data[r - 1] = self.fn(self.data[r - 1], x)
                r -= 1
            l //= 2
            r //= 2

    # i番目の要素の値を取得する
    def query(self, i):  # O(logN)
        i += len(self.data) // 2
        ret = self.data[i]
        while i > 0:
            i //= 2
            ret = self.fn(ret, self.data[i])
        return ret

