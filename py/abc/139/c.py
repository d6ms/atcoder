N = int(input())
H = list(map(int, input().split()))

r = 0
l = 0
ans = 0
while r < N:
    if r < N - 1 and H[r + 1] <= H[r]:
        r += 1
        ans = max(ans, r - l)
    elif r != l:
        l += 1
    else:
        l += 1
        r += 1
print(ans)