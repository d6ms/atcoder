import numpy as np

N = int(input())
h = np.array(list(map(int, input().split())))


def recurse(arr):
    if len(arr) == 0:
        return 0
    if all([e == 0 for e in arr]):
        return 0

    cnt = 0
    while all([e > 0 for e in arr]):
        arr = arr - 1
        cnt += 1

    next = []
    for e in arr:
        if e != 0:
            next.append(e)
        else:
            cnt += recurse(np.array(next))
            next.clear()
    if len(next) > 0:
        cnt += recurse(np.array(next))

    return cnt


print(recurse(h))
