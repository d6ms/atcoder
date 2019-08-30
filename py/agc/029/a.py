S = input()

ans = 0
cnt = 0
for i, c in enumerate(reversed(S)):
    if c == 'B':
        ans += i - cnt
        cnt += 1
print(ans)
