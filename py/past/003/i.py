import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


N = I()
Q = I()

row = list(range(N))
col = list(range(N))
t = False
for q in [input() for _ in range(Q)]:
    if q.startswith('4'):
        _, A, B = map(lambda s: int(s) - 1, q.split())
        if t:
            i, j = row[B], col[A]
        else:
            i, j = row[A], col[B]
        print(N * i + j)
    elif q.startswith('3'):
        t = not t
    elif q.startswith('2'):
        _, A, B = map(lambda s: int(s) - 1, q.split())
        if t:
            row[A], row[B] = row[B], row[A]
        else:
            col[A], col[B] = col[B], col[A]
    elif q.startswith('1'):
        _, A, B = map(lambda s: int(s) - 1, q.split())
        if t:
            col[A], col[B] = col[B], col[A]
        else:
            row[A], row[B] = row[B], row[A]
