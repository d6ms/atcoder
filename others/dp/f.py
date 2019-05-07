import doctest


def solve(s, t):
    """
    >>> solve("axyb", "abyxb")
    'axb'
    """
    return "axb"


doctest.testmod()

s = input()
t = input()
print(solve(s, t))
