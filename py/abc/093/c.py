import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


A, B, C = MI()
m = max(A, B, C)

ans = (m - A) // 2
A += (m - A) // 2 * 2
ans += (m - B) // 2
B += (m - B) // 2 * 2
ans += (m - C) // 2
C += (m - C) // 2 * 2

d = 3 * m - (A + B + C)
if d == 0:
    print(ans)
elif d == 1:
    print(ans + 2)
else:
    print(ans + 1)
