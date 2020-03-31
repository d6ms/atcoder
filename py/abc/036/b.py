import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = I()
S = [list(input()) for _ in range(N)]

ans = [['' for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        ans[j][N - 1 - i] = S[i][j]

for l in ans:
    print(''.join(l))