from math import ceil


K = int(input())
X, Y = map(int, input().split())

if K % 2 == 0 and (X + Y) % 2 == 1:
    print(-1)
    exit(0)


N = ceil((X + Y) / K)  # N回の移動でたどり着ける

