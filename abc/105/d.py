N, M = map(int, input().split())
A = list(map(int, input().split()))


def to_cumsum(arr):
    cumsum = 0
    new = list()
    for e in arr:
        cumsum = (cumsum + e) % M
        new.append(cumsum)
    return new


d = dict()
for a in to_cumsum(A):
    if d.get(a) is None:
        d[a] = 1
    else:
        d[a] += 1

ans = 0
for mod, cnt in d.items():
    if mod == 0:
        ans += cnt
    ans += cnt * (cnt - 1) // 2
print(ans)
