import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


s = input()
t = input()

if s == t:
    print('same')
elif s.lower() == t.lower():
    print('case-insensitive')
else:
    print('different')