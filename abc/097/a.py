a, b, c, d = map(int, input().split())
p = [a, b, c]
p.sort()

if abs(a - c) <= d:
    print('Yes')
elif p[1] - p[0] <= d and p[2] - p[1] <= d:
    print('Yes')
else:
    print('No')
