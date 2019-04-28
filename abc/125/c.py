import fractions


def solve(N, A):
    max_gcd = 0
    gcd1memo = [None] * N  # gcd [0, i]
    gcd2memo = [None] * N  # gcd [i, N - 1]
    gcd1memo[0] = A[0]
    gcd2memo[N - 1] = A[N - 1]
    for i in range(1, N):
        gcd1memo[i] = fractions.gcd(gcd1memo[i - 1], A[i])
    for i in reversed(range(N - 1)):
        gcd2memo[i] = fractions.gcd(gcd2memo[i + 1], A[i])
    for i in range(N):
        gcd = None
        if i == 0:
            gcd = gcd2memo[1]
        elif i == N - 1:
            gcd = gcd1memo[N - 1]
        else:
            gcd = fractions.gcd(gcd1memo[i - 1], gcd2memo[i + 1])
        max_gcd = max(max_gcd, gcd)
    return max_gcd


N = int(input())
A = list(map(int, input().split()))
print(solve(N, A))
