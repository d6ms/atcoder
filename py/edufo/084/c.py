import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


n, m, k = MI()
XY = [tuple(MI()) for _ in range(k)]
for i in range(k):
    input()

mx = max(x for x, y in XY)
my = max(y for x, y in XY)

ans = ''
ans += 'L' * (my - 1)
ans += 'U' * (mx - 1)
for i in range(m):
    ans += ('R' if i % 2 == 0 else 'L') * n
    if i < m - 1:
        ans += 'D'
print(ans)