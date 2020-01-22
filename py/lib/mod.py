# 乗算
def mul(a, b, mod=10 ** 9 + 7):
    return (a % mod) * (b % mod) % mod


# 除算
# a / b = a * b^(-1)
def div(a, b, mod=10 ** 9 + 7):
    return (a % mod) * pow(b, mod - 2, mod) % mod


# Nの逆元を求める
# N^(-1) = N^(MOD-2) % MOD
def inverse(n, mod=10 ** 9 + 7):
    return pow(n, mod - 2, mod)


# 累乗
def power(x, y, mod=10 ** 9 + 7):
    if y == 0:
        return 1
    elif y == 1:
        return x % mod
    elif y % 2 == 0:
        return power(x, y / 2) ** 2 % mod
    else:
        return power(x, y / 2) ** 2 * x % mod


# 階乗とその逆元を事前計算する (O(N))
# finv[0] := 0の階乗の逆元
def factorial_and_inv(n, mod=10 ** 9 + 7):
    f = [1]
    for n in range(1, n):
        f.append(f[n - 1] * n % mod)
    finv = [0] * n
    finv[n - 1] = pow(f[n - 1], mod - 2, mod)
    for n in range(n - 2, -1, -1):
        finv[n] = finv[n + 1] * (n + 1) % mod
    return f, finv
