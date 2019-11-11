S = input()

ans = 0
power = 0
for s in S:
    if power == 0:
        if s == 'g':
            power += 1
        else:
            power += 1
            ans -= 1
        continue
    if s == 'g':
        ans += 1
        power -= 1
    else:
        power -= 1
print(ans)
