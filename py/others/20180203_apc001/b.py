import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')

N = I()
A = LMI()
B = LMI()

cnt = 0
for i in range(N):
    cnt += B[i] - A[i]

