A, B = map(int, input().split())

from fractions import gcd

def lcm(a, b):
    """
    aとbの最小公倍数を計算します。
    """
    return a * b // gcd(a, b)

print(lcm(A, B))