import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')

N, M = MI()

ans = N * (N - 1) // 2
ans += M * (M - 1) // 2
print(ans)