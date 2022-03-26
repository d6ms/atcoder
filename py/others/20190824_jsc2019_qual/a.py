import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


M, D = MI()
cnt = 0
for m in range(1, M + 1):
    for d in range(1, D + 1):
        d10, d1 = divmod(d, 10)
        if d1 > 1 and d10 > 1 and d1 * d10 == m:
            cnt += 1
print(cnt)