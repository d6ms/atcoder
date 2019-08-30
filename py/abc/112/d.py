# ND <= M
# D <= M // N
# DはMの約数


def divisors(n):
    """
    nの約数をO(√n)で列挙する
    """
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors


N, M = map(int, input().split())
ans = 0
for D in divisors(M):
    if ans < D <= M // N:
        ans = D
print(ans)
