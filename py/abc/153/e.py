from fractions import Fraction

H, N = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]

ma, mb = None, None
m_cospa = 0
for a, b in AB:
    cospa = Fraction(a, b)
    if cospa > m_cospa:
        ma, mb = a, b
        m_cospa = cospa

ans = H // ma * mb
H %= ma

if H == 0:
    print(ans)
    exit(0)

min_pow = float('inf')
for a, b in AB:
    if a >= H:
        mp = b
    elif H % a == 0:
        mp = H // a * b
    else:
        mp = (H // a + 1) * b
    min_pow = min(min_pow, mp)
ans += min_pow
print(ans)