S = input()

ans = 0
for c in S:
    if c == '+':
        ans += 1
    elif c == '-':
        ans -= 1
print(ans)
