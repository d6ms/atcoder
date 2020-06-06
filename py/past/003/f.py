import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = I()
A = []

for i in range(-(-N // 2)):
    A.append(set(input()))
for i in range(-(-N // 2), N):
    pair = N - i - 1
    A[pair].intersection_update(set(input()))

if any(len(s) == 0 for s in A):
    print(-1)
else:
    half = ''.join(s.pop() for s in A)
    ans = half
    if N % 2 == 1:
        half = half[:-1]
    ans += ''.join(list(reversed(half)))
    print(ans)