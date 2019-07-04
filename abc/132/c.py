N = int(input())
D = list(map(int, input().split()))
D.sort()

count = 0
cur = 0
for i in range(10**5 + 1):
    if cur == N / 2:
        count += 1
    if cur > N / 2:
        break
    if D[cur] < i and cur < N:
        cur += 1
        while D[cur - 1] == D[cur]:
            cur += 1
print(count)
