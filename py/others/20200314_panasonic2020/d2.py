import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7


s = 'abcdefghijklmnop'
N = I()


def f(n, seq, m):
    for i in range(m + 1):
        if n == N:
            print(seq + s[i])
        else:
            f(n + 1, seq + s[i], max(m, i + 1))


f(1, '', 0)
