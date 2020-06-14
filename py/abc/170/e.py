import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI0(): return map(lambda s: int(s) - 1, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
def LMI0(): return list(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
from heapq import heappush, heappop
INF = float('inf')

class MultiSet(object):

    def __init__(self, arr=None):
        self.p = list()
        self.q = list()
        if arr is not None:
            for x in arr:
                heappush(self.p, x)

    def add(self, x):  # O(logN)
        heappush(self.p, x)

    def remove(self, x):  # O(logN)
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

    def __len__(self):
        while self.q and self.p[0] == self.q[0]:
            heappop(self.p)
            heappop(self.q)
        return len(self.p)


N, Q = MI()
AB = [tuple(MI()) for _ in range(N)]
CD = [tuple(MI0()) for _ in range(Q)]


# schoolを座圧
zaatu = set()
for _, b in AB:
    zaatu.add(b - 1)
for _, d in CD:
    zaatu.add(d)
zaatu = sorted(list(zaatu))
n_school = len(zaatu)
map_school = dict()
for i, sc in enumerate(zaatu):
    map_school[sc] = i

school = [MultiSet() for _ in range(n_school)]
rate = [0] * N
belong = [0] * N
maxRate = [None for _ in range(n_school)]
for i, (A, B) in enumerate(AB):
    B = map_school[B - 1]
    rate[i] = A
    belong[i] = B
    school[B].add(-A)

ans = MultiSet()

for s in school:
    if len(s) > 0:
        ans.add(-s.peek())

for C, D in CD:
    S = belong[C]
    D = map_school[D]

    src_max = school[S].peek()
    ans.remove(-src_max)
    dst_max = school[D].peek()
    if dst_max is not None:
        ans.remove(-dst_max)
        
    school[S].remove(-rate[C])
    school[D].add(-rate[C])
    belong[C] = D
    
    src_max = school[S].peek()
    if src_max is not None:
        ans.add(-src_max)
    dst_max = school[D].peek()
    ans.add(-dst_max)

    print(ans.peek())
