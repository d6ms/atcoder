from bisect import bisect_left, bisect_right

N = int(input())
L = list(map(int, input().split()))

L.sort()
ans = 0

for a in range(N):
    for b in range(a + 1, N):
        c = bisect_left(L, L[a] + L[b])
        ans += c - b - 1
print(ans)
