def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))
MOD=10 ** 9 + 7
n, a, b = MI()

ans = (pow(2, n, MOD) - 1) % MOD
def combination(n, r, mod=10**9+7):
    n1, r = n+1, min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod-2, mod) % mod
ans -= combination(n, a)
ans -= combination(n, b)
print(ans % MOD)
