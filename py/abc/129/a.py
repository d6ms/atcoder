P, Q, R = map(int, input().split())

ans = float('inf')
ans = min(ans, P + Q)
ans = min(ans, R + Q)
ans = min(ans, P + R)
ans = min(ans, Q + R)
ans = min(ans, Q + P)
ans = min(ans, Q + P)

print(ans)