from heapq import heapify, heappush, heappop


class AscKeyMappedPriorityQueue(object):

    def __init__(self, arr=None, key_generator=lambda x: x):
        """
        昇順以外のソートをheapqで実現することはできず、昇順になるキーを挿入する値から作る必要がある。
        tupleの扱いやらが面倒なのでオブジェクトとしてpush, pop操作を簡易に行えるようにしている。
        :param arr: ヒープ化する元の配列が存在する場合は指定する
        :param key_generator: 挿入する値から昇順になるようなキーを作る関数
        """
        self.key_generator = key_generator
        if arr:
            self.arr = [(key_generator(e), e) for e in arr]
            heapify(self.arr)
        else:
            self.arr = []

    def push(self, e):
        heappush(self.arr, (self.key_generator(e), e))

    def pop(self):
        return heappop(self.arr)[1]
