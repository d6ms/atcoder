H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

arr = list()
for i, a in enumerate(A):
    for j in range(a):
        arr.append(i + 1)
for i in range(H):
    sub = arr[i * W: (i + 1) * W]
    if i % 2 == 1:
        sub = list(reversed(sub))
    print(' '.join([str(x) for x in sub]))