def primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


N = int(input())
ans = list()
for p in primes():
    if len(ans) >= N:
        break
    if p % 5 == 1:
        ans.append(p)

print(' '.join([str(p) for p in ans]))