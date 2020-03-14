import sys
from math import sqrt

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


a, b, c = MI()
if c - b - a <= 0:
    print('No')
    exit(0)
r = (c - b - a) ** 2
l = 4 * a * b
if l < r:
    print('Yes')
else:
    print('No')
