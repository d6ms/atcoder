import sys
sys.setrecursionlimit(300000)
from decimal import Decimal, getcontext
getcontext().prec = 32

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')
from math import floor

A, B = input().split()
A = Decimal(A)
B = Decimal(B)
print(floor(A * B))