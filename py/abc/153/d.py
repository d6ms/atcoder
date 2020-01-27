H = int(input())

memo = dict()

def f(n):
    if memo.get(n) is not None:
        return memo[n]
    if n == 1:
        return 1
    val = 1 + 2 * f(n // 2)
    memo[n] = val
    return val

print(f(H))