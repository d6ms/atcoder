import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')

N = I()
if N <= 59:
    print('Bad')
elif N <= 89:
    print('Good')
elif N <= 99:
    print('Great')
else:
    print('Perfect')