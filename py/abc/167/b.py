import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


A, B, C, K = MI()
if K <= A:
    print(K)
elif K <= A + B:
    print(A)
else:
    print(A - (K - (A + B)))
