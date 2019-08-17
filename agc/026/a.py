N = int(input())
A = list(map(int, input().split()))

cnt = 0
for i in range(1, N):
    if A[i] == A[i - 1]:
        A[i] = 10001
        cnt += 1
print(cnt)