N = int(input())
A = list(map(int, input().split()))

A.sort()

m = A[0]
M = A[-1]
ans = list()
for a in A[1: -1]:
    if a < 0:
        ans.append((M, a))
        M = M - a
    else:
        ans.append((m, a))
        m = m - a
ans.append((M, m))
print(M - m)
for x, y in ans:
    print(x, y)