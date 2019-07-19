N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

min_temp = float('inf')
ans = None
for i in range(N):
    temp = abs(A - (T - H[i] * 0.006))
    if min_temp > temp:
        min_temp = temp
        ans = i
print(ans + 1)