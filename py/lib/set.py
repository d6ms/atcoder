from heapq import heappush, heappop


class MultiSet(object):
    """
    重複を許した順序付き集合。
    最小要素の取り出し・削除が共にO(logN)で行えるため、削除を含むheapq的な利用ができる。
    """

    def __init__(self, arr=None):
        self.p = list()
        self.q = list()
        # listからの変換は O(NlogN)
        if arr is not None:
            for x in arr:
                heappush(self.p, x)

    def add(self, x):  # O(logN)
        heappush(self.p, x)

    def remove(self, x):  # O(logN)
        """
        高速化のため、存在しない要素の削除には対応していない(壊れる)。
        必要ならp, qの他に、要素の種類とその個数を管理するdictが必要。
        """
        heappush(self.q, x)

    def poll(self):  # 償却 O(logN)
        while self.q and self.p[0] == self.q[0]:
            heappop(self.p)
            heappop(self.q)
        if self.p:
            result = heappop(self.p)
            return result
        else:
            return None

    def peek(self):  # 償却 O(logN)
        while self.q and self.p[0] == self.q[0]:
            heappop(self.p)
            heappop(self.q)
        if self.p:
            return self.p[0]
        else:
            return None

    def __len__(self):  # 償却 O(logN)
        while self.q and self.p[0] == self.q[0]:
            heappop(self.p)
            heappop(self.q)
        return len(self.p)
