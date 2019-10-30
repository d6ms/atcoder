from math import atan, degrees

a, b, x = map(int, input().split())

if a * a * b / 2 < x:
    tan_theta = 2 * (a * a * b - x) / (a ** 3)
else:
    tan_theta = (a * b * b) / (2 * x)

print(degrees(atan(tan_theta)))
