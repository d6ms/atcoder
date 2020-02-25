def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))
MOD = 10 ** 9 + 7


W, H, N = MI()
m = [0, 0, W, 0, H]
for _ in range(N):
    x, y, a = MI()
    if a == 1:
        m[a] = max(m[a], x)
    elif a == 2:
        m[a] = min(m[a], x)
    elif a == 3:
        m[a] = max(m[a], y)
    else:
        m[a] = min(m[a], y)
print(max(0, m[2] - m[1]) * max(0, m[4] - m[3]))