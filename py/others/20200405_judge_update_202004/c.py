import sys
sys.setrecursionlimit(300000)
from itertools import permutations

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


a1, a2, a3 = MI()
N = a1 + a2 + a3

def is_ok(p):
    b1, b2, b3 = [INF] * 3, [INF] * 3, [INF] * 3
    i = 0
    for a in p[:a1]:
        b1[i] = a
        i += 1
    i = 0
    for a in p[a1:a1+a2]:
        b2[i] = a
        i += 1
    i = 0
    for a in p[a1+a2:]:
        b3[i] = a
        i += 1
    for b in [b1, b2, b3]:
        for i in range(2):
            if b[i] < INF and b[i + 1] <= b[i]:
                return False
    B = [b1, b2, b3]
    for j in [0, 1, 2]:
        for i in range(2):
            if B[i + 1][j] < INF and B[i + 1][j] <= B[i][j]:
                return False
    return True


cnt = 0
for p in permutations(range(1, N + 1), N):
    if is_ok(p):
        cnt += 1
print(cnt)

