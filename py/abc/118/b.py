N, M = map(int, input().split())

memo = [0 for _ in range(M + 1)]
for i in range(N):
    A = list(map(int, input().split()))[1:]
    for a in A:
        memo[a] += 1

ans = len(list(filter(lambda x: x == N, memo)))
print(ans)