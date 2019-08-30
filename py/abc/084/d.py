def primes():
    """
    素数のジェネレータ
    """
    d = {}
    q = 2
    while True:
        if q not in d:
            yield q
            d[q * q] = [q]
        else:
            for p in d[q]:
                d.setdefault(p + q, []).append(p)
            del d[q]
        q += 1


p = set()
for num in primes():
    if num > 100001:
        break
    p.add(num)

memo = [0 for _ in range(100001)]
for i in range(1, 100001):
    if i % 2 == 0:
        memo[i] = memo[i - 1]
        continue
    if i in p and (i + 1) // 2 in p:
        memo[i] = memo[i - 1] + 1
    else:
        memo[i] = memo[i - 1]

Q = int(input())
lr = [tuple(map(int, input().split())) for _ in range(Q)]
for l, r in lr:
    print(memo[r] - memo[l - 1])
