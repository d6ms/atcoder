A, B, C = map(int, input().split())
m = A % B
org = m
m = (m + m) % B
while m != org:
    if m == C:
        print('YES')
        exit(0)
    m = (m + org) % B
print('NO')