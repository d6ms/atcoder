def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))


MOD = 10 ** 9 + 7
N, M = MI()
if abs(N - M) > 1:
    print(0)
    exit(0)

f = [1]
for n in range(1, max(N, M) + 1):
    f.append(f[n - 1] * n % MOD)
print(f[N] * f[M] * (2 if abs(N - M) == 0 else 1) % MOD)
