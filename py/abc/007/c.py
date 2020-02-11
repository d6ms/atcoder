from collections import deque


def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))


H, W = MI()
sy, sx = MI()
gy, gx = MI()
maze = [input() for _ in range(H)]
sy, sx, gy, gx = sy - 1, sx - 1, gy - 1, gx - 1

q = deque()
q.append((sy, sx, 0, -1, -1))
seen = {sx * W + sy}
while len(q) > 0:
    y, x, d, py, px = q.popleft()
    if y == gy and x == gx:
        print(d)
        exit(0)
    for dy, dx in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
        next_y, next_x = y + dy, x + dx
        if next_y * W + next_x not in seen and maze[next_y][next_x] == '.':
            seen.add(next_y * W + next_x)
            q.append((next_y, next_x, d + 1, y, x))
