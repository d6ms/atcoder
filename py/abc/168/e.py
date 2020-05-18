import sys
sys.setrecursionlimit(300000)
from fractions import Fraction
from collections import defaultdict

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = I()
d2 = defaultdict(int)
AB = list()
for i in range(N):
    a, b = MI()
    AB.append((a, b))
    d2[(-b, a)] += 1
hate = [0] * N
for i in range(N):
    a, b = AB[i]
    hate[i] = d2[(-b, a)]

# [今まで選んだイワシの番号], 残りの選べる引数
stack = [([], N)]
while len(stack) > 0:
    chosen, remain = stack.pop()
