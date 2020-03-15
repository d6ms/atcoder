import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


X, Y = MI()

w = [0, 300000, 200000, 100000]
ans = 0
ans += w[X] if X <= 3 else 0
ans += w[Y] if Y <= 3 else 0
if X == 1 and Y == 1:
    ans += 400000
print(ans)
