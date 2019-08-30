N, X = map(int, input().split())
L = list(map(int, input().split()))

D = 0
i = 1
for l in L:
    D += l
    if D > X:
        break
    i += 1
print(i)
