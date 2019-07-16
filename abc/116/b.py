s = int(input())


def f(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return 3 * n + 1


d = dict()
d[s] = 1
an = s
i = 2
while True:
    an = f(an)
    if d.get(an) is not None:
        print(i)
        break
    d[an] = i
    i += 1