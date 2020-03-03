import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


N, M = MI()
d = {i: 0 for i in range(N)}
for _ in range(M):
    a, b = MI()
    d[a - 1] += 1
    d[b - 1] += 1
for i in range(N):
    print(d[i])
