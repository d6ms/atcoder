from collections import defaultdict


def to_cumsum(arr):
    arr.sort(reverse=True)
    cumsum = 0
    new = [0] * (len(arr) + 1)
    for i, e in enumerate(arr):
        cumsum += e
        new[i + 1] = cumsum
    return new


N, W = map(int, input().split())

weights = defaultdict(int)
values = defaultdict(list)
for i in range(N):
    w, v = map(int, input().split())
    weights[w] += 1
    values[w].append(v)
for k, v in values.items():
    values[k] = to_cumsum(v)

w1 = min(weights.keys())
w2 = w1 + 1
w3 = w2 + 1
w4 = w3 + 1
for w in [w1, w2, w3, w4]:
    if len(values[w]) == 0:
        values[w] = [0]

ans = 0
for i1 in range(weights[w1] + 1):
    for i2 in range(weights[w2] + 1):
        for i3 in range(weights[w3] + 1):
            for i4 in range(weights[w4] + 1):
                if w1 * i1 + w2 * i2 + w3 * i3 + w4 * i4 > W:
                    continue
                ans = max(ans, values[w1][i1] + values[w2][i2] + values[w3][i3] + values[w4][i4])
print(ans)
