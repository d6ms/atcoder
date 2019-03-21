# WA and LTE


def solve(K, X_Y_C):
    # 白の左上が来る座標を(x, y)として全塗りつぶしパターンで探索
    max_achieved_count = 0
    for x in range(K):
        for y in range(2 * K):
            achieved_count = get_achieved_count(K, X_Y_C, x, y)
            if achieved_count > max_achieved_count:
                max_achieved_count = achieved_count
    return max_achieved_count


def get_achieved_count(K, X_Y_C, x, y):
    achieved_count = 0
    for x_y_c in X_Y_C:
        adj_x = int(x_y_c[0]) % (2 * K)
        adj_y = int(x_y_c[1]) % (2 * K)
        c = x_y_c[2]

        dist_x = abs(adj_x - x)
        dist_y = abs(adj_y - y)

        is_white = ((dist_x // K) + (dist_y // K)) % 2 == 0
        if (is_white and c == "W") or (not is_white and c == "B"):
            achieved_count += 1
    return achieved_count


N, K = map(int, input().split())
X_Y_C = [list(input().split()) for _ in range(N)]

print(solve(K, X_Y_C))