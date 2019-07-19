N = int(input())
xyh = [tuple(map(int, input().split())) for _ in range(N)]

xi, yi, hi = None, None, None
for x, y, h in xyh:
    if h > 0:
        xi, yi, hi = x, y, h
        break

for cx in range(101):
    for cy in range(101):
        H = hi + abs(xi - cx) + abs(yi - cy)
        matched = True
        for x, y, h in xyh:
            if h != max(H - abs(x - cx) - abs(y - cy), 0):
                matched = False
                break
        if matched:
            print(cx, cy, H)
            exit(0)
