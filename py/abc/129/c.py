N, M = map(int, input().split())
broken = set()
for _ in range(M):
    a = int(input())
    broken.add(a)

INF = 10 ** 9 + 7

memo = [None for _ in range(N + 1)]
memo[0] = 1
memo[1] = 0 if 1 in broken else 1
for i in range(2, N + 1):
    if i in broken:
        memo[i] = 0
    else:
        memo[i] = (memo[i - 2] + memo[i - 1]) % INF

print(memo[N])
