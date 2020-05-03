import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N, M = MI()
if N % 2 != 0:
    for i in range(1, M + 1):
        print(i, 2 * M - i + 1)
else:
    print(2, 1)
    for i in range(3, M + 2):
        print(i, 2 * M - i + 3)
