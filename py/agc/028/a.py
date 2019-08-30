from fractions import gcd


def lcm(a, b):
    """
    aとbの最小公倍数を計算します。
    """
    return a * b // gcd(a, b)


N, M = map(int, input().split())
S = input()
T = input()

ans = lcm(N, M)

c = dict()
for i in range(N):
    c[i * ans // N] = S[i]
for i in range(M):
    val = c.get(i * ans // M)
    if val is not None and val != T[i]:
        print(-1)
        exit(0)
print(ans)