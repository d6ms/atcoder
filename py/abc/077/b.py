from math import sqrt

def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))
MOD = 10 ** 9 + 7


N = I()
rt = sqrt(N)
if rt.is_integer():
    print(N)
else:
    print(int(rt) ** 2)
