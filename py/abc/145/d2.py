MOD = 10 ** 9 + 7


def combination(n, r, mod=10**9+7):
    n1, r = n+1, min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod-2, mod) % mod


X, Y = map(int, input().split())

# a := →→↑ の個数
# b := →↑↑ の個数
# 2a + b = X
# a + 2b = Y より、
a = (2 * X - Y) / 3
b = (2 * Y - X) / 3

if a < 0 or b < 0 or not a.is_integer() or not b.is_integer():
    print(0)
    exit(0)

ans = combination(int(a + b), int(a), mod=MOD)
print(ans)
