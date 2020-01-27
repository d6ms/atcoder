from fractions import Fraction

H, N = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]

ma, mb = None, None
m_cospa = 0
for a, b in AB:
    cospa = Fraction(a, b)
    if cospa > m_cospa or (cospa == m_cospa and a < ma):
        ma, mb = a, b
        m_cospa = cospa
if H % ma == 0:
    print((H // ma) * mb)
    exit(0)

mans = float('inf')
for a, b in AB:
    for i in range(1, H // a + 2):
        ans = 0
        hp = H
        hp -= (a * i)
        ans += b * i
        if hp > 0:
            if hp % ma == 0:
                ans += (hp // ma) * mb
            else:
                ans += (hp // ma + 1) * mb
        mans = min(mans, ans)
print(mans)