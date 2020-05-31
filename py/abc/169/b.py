import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = I()
A = LMI()
ans = 1
th = 10 ** 18
if 0 in A:
    print(0)
    exit()
for a in A:
    ans *= a
    if ans > th:
        print(-1)
        exit()
print(ans)
