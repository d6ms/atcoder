N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7

if K == 1:
    print(0)
    exit(0)

A.sort()
s = 0
for i in range(N):
    plus_times = max(0, i - K + 2)
    minus_times = 0 if i + K > N else N - i - 1
    s = s + (plus_times * A[i])
    s = s - (minus_times * A[i])
    s %= MOD
print(s)
