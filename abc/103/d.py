N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]

AB.sort(key=lambda ab: ab[1])
removed = list()
for a, b in AB:
    if len(removed) == 0:
        removed.append(b - 1)
    elif a <= removed[-1] < b:
        continue
    else:
        removed.append(b - 1)
print(len(removed))