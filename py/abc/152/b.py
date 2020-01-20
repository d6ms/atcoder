a, b = map(int, input().split())
ans = min(str(a) * b, str(b) * a)
print(ans)