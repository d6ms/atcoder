import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


x, y = MI()

g1 = {1, 3, 5, 7, 8, 10, 12}
g2 = {4, 6, 9, 11}
if (x in g1 and y in g1) or (x in g2 and y in g2) or x == y == 2:
    print('Yes')
else:
    print('No')
