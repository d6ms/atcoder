N, K = map(int, input().split())

if K == 0:
    print(N * N)
    exit(0)

cnt = 0
for b in range(K + 1, N + 1):
    p = N // b
    r = N % b
    cnt += p * max(0, b - K)
    cnt += max(0, r - K + 1)
print(cnt)
