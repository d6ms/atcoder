N = int(input())


def f(s):
    for c in ['a', 'b', 'c']:
        next = s + c
        if len(next) == N:
            print(next)
        else:
            f(next)


f('')
