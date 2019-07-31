N = int(input())

if N == 0:
    print(0)
    exit(0)

ans = ''
while N != 0:
    r = abs(N % 2)
    N = (N - r) // -2
    ans += str(r)

print(''.join(reversed(ans)))