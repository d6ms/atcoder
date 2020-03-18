import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = I()
A = input()
B = input()
C = input()

ans = 0
for i in range(N):
    if A[i] == B[i] == C[i]:
        continue
    if A[i] == B[i] or B[i] == C[i] or C[i] == A[i]:
        ans += 1
    else:
        ans += 2
print(ans)

