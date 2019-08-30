D, G = map(int, input().split())
P = list()
for i in range(1, D + 1):
    p, c = map(int, input().split())
    P.append((100 * i, p, c))

ans = float('inf')
for i in range(2 ** D):
    points = 0
    problems = 0
    for d in range(D):
        if (i >> d) & 1:
            i100, p, c = P[d]
            points += i100 * p + c
            problems += p
    if points >= G:
        ans = min(ans, problems)
        continue
    for d in reversed(range(D)):
        if (i >> d) & 1:
            continue
        i100, p, c = P[d]
        for j in range(p):
            if points >= G:
                break
            points += i100
            problems += 1
    ans = min(ans, problems)

print(ans)
