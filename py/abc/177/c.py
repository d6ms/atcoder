MOD = 10 ** 9 + 7

N = int(input())
A = list(map(int, input().split()))

ans = 0
s = sum(A)
for a in A:
    s -= a
    ans = (ans + ((s % MOD) * a % MOD)) % MOD
print(ans)