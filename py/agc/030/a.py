A, B, C = map(int, input().split())

ans = 0
if B <= C:
    ans += 2 * B
    C -= B
    if A < C:
        ans += A + 1
    else:
        ans += C
else:
    ans += 2 * C
    ans += B - C
print(ans)