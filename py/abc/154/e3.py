def I(): return int(input())


def MI(): return map(int, input().split())


def LMI(): return list(map(int, input().split()))


def combination(n, r, mod=10 ** 9 + 7):
    n1, r = n + 1, min(r, n - r)
    numer = denom = 1
    for i in range(1, r + 1):
        numer = numer * (n1 - i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod - 2, mod) % mod


# dp[i + 1][smaller][j] = 上からi桁目までで0でない桁がj個ある数字の数
N = input()
K = I()
l = len(N)
dp = [[[0] * (K + 1) for _ in range(2)] for _ in range(l)]
ans = 0
for i in range(l):
    for smaller in [True, False]:  # smaller := Nより小さいことが確定している
        for j in range(1, K + 1):
            # if i == 0 and not smaller:
            #     continue
            if smaller:
                dp[i][smaller][j] += dp[i - 1][smaller]
                dp[i][smaller] += 9 * combination(l - i - 1, j - 1)
            else:
                dp[i][smaller][j] += int(N[i]) * combination(l - i - 1, j - 1)
print(dp)
print(dp[l - 1][True][K] + dp[l - 1][False][K])
