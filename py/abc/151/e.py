
class BinomialCoefficient(object):

    def __init__(self, N=510000, MOD=10**9+7):
        self.fac = [1, 1]
        self.finv = [1, 1]
        self.inv = [0, 1]
        self.MOD = MOD
        for i in range(2, N + 1):
            self.fac.append((self.fac[-1] * i) % MOD)
            self.inv.append((-self.inv[MOD % i] * (MOD // i)) % MOD)
            self.finv.append((self.finv[-1] * self.inv[-1]) % MOD)

    def comb(self, n, r):
        if r < 0 or n < r or r < 0:
            return 0
        return self.fac[n] * self.finv[r] * self.finv[n - r] % self.MOD


N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7

A.sort()
bc = BinomialCoefficient(N)
nCk = bc.comb(N, K)
ans = 0
for i in range(N - 1):
    c = nCk - bc.comb(i + 1, K) - bc.comb((N - i - 1), K)
    ans += c * (A[i + 1] - A[i]) % MOD
    ans %= MOD
print(ans)
