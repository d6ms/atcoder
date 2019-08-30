def divisors(n, sort=False):
    """
    nの約数をO(√n)で列挙する
    """
    d = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            d.append(i)
            if i != n // i:
                d.append(n//i)
    if sort:
        d.sort()
    return d


C = [list(map(int, input().split())) for _ in range(3)]
if sum([sum(r) for r in C]) == 0:
    print('Yes')
    exit(0)

for a0 in divisors(sum(C[0])):
    a = [a0, None, None]
    b = [None, None, None]
    b[0] = C[0][0] - a[0]
    a[1] = C[1][0] - b[0]
    a[2] = C[2][0] - b[0]
    b[1] = C[0][1] - a[0]
    b[2] = C[0][2] - a[0]
    ok = True
    for i in range(3):
        for j in range(3):
            if C[i][j] != a[i] + b[j]:
                ok = False
    if ok:
        print('Yes')
        exit(0)
print('No')