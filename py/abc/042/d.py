H, W, A, B = map(int, input().split())
MOD = 10 ** 9 + 7

i = H - A - 1
j = B


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


f, finv = factorial_and_inv(W + H + 2, MOD)
ans = 0
while i >= 0 and W > j:
    path1 = f[i + j] * finv[i] % MOD * finv[j] % MOD
    path2 = f[(H - i - 1) + (W - j - 1)] * finv[H - i - 1] % MOD * finv[W - j - 1] % MOD
    ans += path1 * path2 % MOD
    i -= 1
    j += 1
print(ans % MOD)
