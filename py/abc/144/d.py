from math import tan, radians


a, b, x = map(int, input().split())

if a * a * b / 2 < x:
    target = (a * b * b) / (2 * x)
else:
    target = 2 * (b - x) / a

theta = 45
for _ in range(10000):
    val = tan(radians(theta))
    if abs(target - val) < 0.1 ** 6:
        break
    elif val < target:
        theta = min(90, theta + theta / 2)
    else:
        theta = max(0, theta - theta / 2)

print(theta)