from operator import xor

A, B = map(int, input().split())


def f(n):
    if n % 2 == 0:
        if n % 4 == 0:
            return n
        else:
            return xor(n, 1)
    else:
        return xor(n, f(n - 1))


print(xor(f(A - 1), f(B)))

# 0,   1,   2,   3,   4,   5,   6,   7
# 000, 001, 010, 011, 100, 101, 110, 111
# 000, 001, 011, 000, 100, 001, 000, 111
# f(A, B) = f(0, A - 1) ^ f(0, B)
# f(0, X) = X ^ (X - 1)
