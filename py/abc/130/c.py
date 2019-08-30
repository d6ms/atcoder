W, H, x, y = map(int, input().split())

max_S = W * H / 2
hukusu = 1 if x == W / 2 and y == H / 2 else 0

print(max_S, hukusu)
