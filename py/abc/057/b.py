import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, M = MI()
AB = [tuple(MI()) for _ in range(N)]
CD = [tuple(MI()) for _ in range(M)]
for a, b in AB:
    min_dist = INF
    ans = 0
    for i, (c, d) in enumerate(CD):
        dist = abs(a - c) + abs(b - d)
        if dist < min_dist:
            min_dist = dist
            ans = i + 1
    print(ans)