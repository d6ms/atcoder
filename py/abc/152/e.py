from fractions import gcd
from functools import reduce
import sys

input = sys.stdin.readline
MOD = 10 ** 9 + 7


def inverse(n, mod=10 ** 9 + 7):
    return pow(n, mod - 2, mod)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    L = reduce(lambda o1, o2: o1 // gcd(o1, o2) * o2, A)
    sigma_A_inv = sum([inverse(a) for a in A])

    print(L * sigma_A_inv % MOD)


if __name__ == '__main__':
    main()
