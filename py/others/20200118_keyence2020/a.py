H = int(input())
W = int(input())
N = int(input())

if N % max(H, W) == 0:
    print(N // max(H, W))
else:
    print(N // max(H, W) + 1)
