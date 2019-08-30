N = int(input())
P = list(map(int, input().split()))

cnt = 0
for i in range(N - 2):
    if P[i+1] != min(P[i:i+3]) and P[i+1] != max(P[i:i+3]):
        cnt += 1
print(cnt)