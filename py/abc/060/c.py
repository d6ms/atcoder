N, T = map(int, input().split())
t = list(map(int, input().split()))

stop = 0
for i in range(1, N):
    stop += max(0, t[i] - (t[i - 1] + T))

print(t[-1] + T - stop)