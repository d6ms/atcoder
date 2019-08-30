# 0位置からの計算でも途中位置からの計算でも計算コストは同じ
def travelable(t, x, y):
    min_step = x + y
    if t < min_step:
        return False
    return (t - min_step) % 2 == 0

ans = None
N = int(input())
for _ in range(N):
    t_x_y = list(map(int, input().split()))
    if not travelable(t_x_y[0], t_x_y[1], t_x_y[2]):
        ans = "No"
        break
if ans is None:
    ans = "Yes"
print(ans)
