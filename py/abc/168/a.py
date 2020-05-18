import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = input()
if N[-1] in '24579':
    print('hon')
elif N[-1] in '0168':
    print('pon')
else:
    print('bon')
