import sys
from decimal import Decimal, getcontext
getcontext().prec = 32


def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


L = Decimal(I())

a = L / Decimal(3)
b = L / Decimal(3)
c = L - a - b

print(a * b * c)
