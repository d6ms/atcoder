W, H, x, y = map(int, input().split())

# W < H => x = xで分割
# W > H => y = yで分割
ans = 1 if W == H else 0
if W < H:
    print(H * min(H - x, x), ans)
else:
    print(W * min(W - y, y), ans)