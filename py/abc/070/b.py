A, B, C, D = map(int, input().split())

ans = max(0, min(B, D) - max(A, C))
print(ans)