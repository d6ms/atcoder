import sys

sys.setrecursionlimit(300000)

N = int(input())

memo = [None for _ in range(N + 1)]


def f(n):
    if n == 0:
        return 0
    if memo[n] is not None:
        return memo[n]
    ans = n
    pow = 1
    while pow <= n:
        ans = min(ans, f(n - pow) + 1)
        pow *= 6
    pow = 1
    while pow <= n:
        ans = min(ans, f(n - pow) + 1)
        pow *= 9
    memo[n] = ans
    return ans


print(f(N))