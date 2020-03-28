import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


X = I()

ans = 0
ans += (X // 500) * 1000
X -= (X // 500) * 500
ans += (X // 5) * 5
print(ans)