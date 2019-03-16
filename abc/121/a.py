H, W = map(int, input().split())
h, w = map(int, input().split())

blacks = (h * W) + (w * H) - (h * w)
whites = H * W - blacks

print(whites)