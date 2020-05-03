import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


K = I()
A, B = MI()

for i in range(A, B + 1):
    if i % K == 0:
        print('OK')
        exit(0)
print('NG')