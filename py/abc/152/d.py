from collections import defaultdict

N = int(input())

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


bc = BinomialCoefficient(N)
d = dict()
for i in range(1, N + 1):
    key = str(i)[0] + str(i)[-1]
    if d.get(key) is None:
        d[key] = 1
    else:
        d[key] += 1

ans = 0
for k, v1 in d.items():
    v2 = d.get(k[1] + k[0])
    if v2 is not None:
        ans += v1 * v2

print(ans)
