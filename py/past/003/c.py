import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


A, R, N = MI()
if R == 1:
    print(A)
    exit(0)
an = A
for _ in range(N - 1):
    an = an * R
    if an > 10 ** 9:
        print('large')
        exit(0)
print(an)