import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


A, B, K = MI()

ans = set(x for x in range(A, A + K) if A <= x <= B)
ans.update(set(x for x in range(B - K + 1, B + 1) if A <= x <= B))
for x in sorted(list(ans)):
    print(x)
