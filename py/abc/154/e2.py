def I(): return int(input())


def MI(): return map(int, input().split())


def LMI(): return list(map(int, input().split()))


def combination(n, r, mod=10 ** 9 + 7):
    if r < 0 or n <= 0:
        return 0
    if r == 0:
        return 1
    n1, r = n + 1, min(r, n - r)
    numer = denom = 1
    for i in range(1, r + 1):
        numer = numer * (n1 - i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod - 2, mod) % mod


# dp[i + 1][smaller][j] = 上からi桁目までで0でない数字がちょうどj個ある数字の数
N = input()
K = I()
l = len(N)
dp = [[[0] * (K + 1) for _ in range(2)] for _ in range(l)]
for i in range(l):
    for smaller in [False, True]:
        for j in range(K + 1):
            dp[i][smaller][j] += dp[i - 1][smaller][j]
            if smaller:
                zeros = N[:i].count('0')
                if j - zeros < 0:
                    continue
                dp[i][smaller][j] += int(N[i]) * combination(l - i - 2, j - zeros)
            else:
                dp[i][smaller][j] += 9 * combination(l - i - 1, j)
print(dp)
print(dp[l - 1][True][K] + dp[l - 1][False][K])