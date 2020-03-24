import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


t = I()
for i in range(t):
    n, k = MI()
    x = (n - (k ** 2)) / 2
    if x.is_integer() and x >= 0:
        print('YES')
    else:
        print('NO')
