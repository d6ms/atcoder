import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


A, B, C, D = MI()
t = -(-C // B)
a = -(-A // D)
print('Yes' if t <= a else 'No')
