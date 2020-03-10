import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


A, B, M = MI()
A = LMI()
B = LMI()

minA = min(A)
minB = min(B)
ans = minA + minB
for _ in range(M):
    x, y, c = MI()
    ans = min(ans, A[x - 1] + B[y - 1] - c)
print(ans)