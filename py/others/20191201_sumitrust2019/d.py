from collections import defaultdict

N = int(input())
S = input()

d = defaultdict(list)
for i, c in enumerate(S):
    d[c].append(i)


def gtmin(arr, num):
    for e in arr:
        if e >= num:
            return e
    return -1


cnt = 0
for i in range(1000):
    num = str(i).zfill(3)
    after = 0
    ok = True
    for digit in num:
        min_val = gtmin(d[digit], after)
        if min_val >= 0:
            after = min_val + 1
        else:
            ok = False
            break
    if ok:
        cnt += 1
print(cnt)
