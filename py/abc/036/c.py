import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = I()
A = [I() for _ in range(N)]

B = [(a, i) for i, a in enumerate(A)]
B.sort()

ans = [0] * N
cur = 0
val = B[0][0]
for b, i in B:
    if b > val:
        val = b
        cur += 1
    ans[i] = cur

for x in ans:
    print(x)