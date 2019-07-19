N, T = map(int, input().split())
c_t = [tuple(map(int, input().split())) for _ in range(N)]

c_t = filter(lambda ct: ct[1] <= T, c_t)
c_t = sorted(c_t, key=lambda ct: ct[0])
if len(c_t) > 0:
    c, t = c_t[0]
    print(c)
else:
    print('TLE')
