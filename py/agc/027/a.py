N, x = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
ans = 0
looped = True
for a in A:
    if x < a:
        looped = False
        break
    x -= a
    ans += 1

if looped and x > 0 and ans > 0:
    ans -= 1

print(ans)