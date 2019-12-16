R, G, B, N = map(int, input().split())

ans = 0
for i in range(N // R + 1):
    rem1 = N - i * R
    for j in range(rem1 // G + 1):
        rem2 = rem1 - j * G
        if rem2 % B == 0:
            ans += 1
print(ans)
