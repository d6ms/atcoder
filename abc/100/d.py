N, M = map(int, input().split())
XYZ = [tuple(map(int, input().split())) for _ in range(N)]


def score(x, y, z, bit):
    s = 0
    s += x if (bit >> 0) & 1 else -x
    s += y if (bit >> 1) & 1 else -y
    s += z if (bit >> 2) & 1 else -z
    return s


ans = 0
for i in range(2 ** 3):
    XYZ.sort(key=lambda xyz: score(xyz[0], xyz[1], xyz[2], i), reverse=True)
    x_sum, y_xum, z_sum = 0, 0, 0
    for x, y, z in XYZ[:M]:
        x_sum += x
        y_xum += y
        z_sum += z
    ans = max(ans, abs(x_sum) + abs(y_xum) + abs(z_sum))

print(ans)
