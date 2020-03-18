import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = I()
d = [tuple(MI()) for _ in range(N)]
d.sort(reverse=True, key=lambda x: x[0] + x[1])

T = 0
A = 0
for i, (a, b) in enumerate(d):
    if i % 2 == 0:
        T += a
    else:
        A += b
print(T - A)