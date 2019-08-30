N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

max_x = max(x)
min_y = min(y)
if max_x < min_y and X < min_y and Y > max_x:
    print('No War')
else:
    print('War')
