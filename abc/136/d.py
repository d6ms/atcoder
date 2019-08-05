S = input()

lst = list()
rev = False
r = 0
l = 0
start = 0
for i in range(len(S)):
    c = S[i]
    if rev and c == 'R':
        lst.append((start, r, l))
        r = 1
        l = 0
        start = i + 1
        rev = False
        continue
    if c == 'R':
        r += 1
    elif c == 'L':
        rev = True
        l += 1
lst.append((start, r, l))

ans = list()
for start, r, l in lst:
    for _ in range(r - 1):
        ans.append(0)

    a = 0
    b = 0
    if r % 2 != 0:
        a += 1
    a += r // 2
    b += r // 2
    if l % 2 != 0:
        b += 1
    a += l // 2
    b += l // 2
    ans.append(a)
    ans.append(b)

    for _ in range(l - 1):
        ans.append(0)

print(' '.join([str(x) for x in ans]))
