S = input()
T = input()

d = dict()
dst = set()
for i, c in enumerate(S):
    if d.get(c) is None:
        if T[i] not in dst:
            d[c] = T[i]
            dst.add(T[i])
        else:
            print('No')
            exit(0)
    elif d[c] == T[i]:
        continue
    else:
        print('No')
        exit(0)
print('Yes')
