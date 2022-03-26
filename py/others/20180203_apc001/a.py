from fractions import gcd


def lcm(a, b):
    """
    aとbの最小公倍数を計算します。
    """
    return a * b // gcd(a, b)


X, Y = map(int, input().split())
a = lcm(X, Y)
if a == X:
    print(-1)
else:
    print(a - X)