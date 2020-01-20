def is_prime(n):
    """
    引数の値が素数であるかを判定する
    """
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


def primes():
    """
    素数のジェネレータ
    """
    d = {}
    q = 2
    while True:
        if q not in d:
            yield q
            d[q * q] = [q]
        else:
            for p in d[q]:
                d.setdefault(p + q, []).append(p)
            del d[q]
        q += 1


def divisors(n, sort=False):
    """
    nの約数をO(√n)で列挙する
    """
    d = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            d.append(i)
            if i != n // i:
                d.append(n//i)
    if sort:
        d.sort()
    return d


def factorize(n):
    """
    nの値を素因数分解し、素因数のリスト形式で返す
    e.g.
    >>> factorize(20)
    [2, 2, 5]
    """
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b += 1
    if n > 1:
        fct.append(n)
    return fct


def factorize2(n):
    """
    nの値を素因数分解し、素因数とその指数をtupleにまとめたリストを返す
    e.g.
    >>> factorize(20)
    [(2, 2), (5, 1)]
    """
    b = 2
    fct = []
    while b * b <= n:
        cnt = 0
        while n % b == 0:
            cnt += 1
            n //= b
        if cnt > 0:
            fct.append((b, cnt))
        b += 1
    if n > 1:
        fct.append((n, 1))
    return fct


def combination(n, r, mod=10**9+7):
    n1, r = n+1, min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod-2, mod) % mod


def create_factorial(n):
    """
    階乗を事前計算した配列を作成します。
    :param n: [0, n]の配列を作成します
    """
    f = list()
    for i in range(n + 1):
        if i in [0, 1]:
            f.append(1)
        else:
            f.append(f[i - 1] * i)
    return f


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


from fractions import gcd

def lcm(a, b):
    """
    aとbの最小公倍数を計算します。
    """
    return a // gcd(a, b) * b
