import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, K = MI()
s = set()
for i in range(K):
    I()
    for a in LMI():
        s.add(a)

ans = 0
for i in range(1, N + 1):
    if i not in s:
        ans += 1
print(ans)

