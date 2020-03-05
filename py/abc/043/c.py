import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


N = I()
A = LMI()

avg = sum(A) // N

ans = float('inf')
for a in [avg - 1, avg, avg + 1]:
    cost = 0
    for b in A:
        cost += (a - b) ** 2
    ans = min(ans, cost)
print(ans)
