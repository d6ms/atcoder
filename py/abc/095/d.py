import sys
input = sys.stdin.readline


def to_cumsum(arr):
    """
    1次元配列を累積和の1次元配列に変換する
    """
    cumsum = 0
    new = [0] * len(arr)
    for i, e in enumerate(arr):
        cumsum += e
        new[i] = cumsum
    return new


def main():
    N, C = map(int, input().split())
    X = [0] * (N + 1)
    X_inv = [0] * (N + 1)
    V = [0] * (N + 1)
    V_inv = [0] * (N + 1)
    for i in range(1, N + 1):
        x, v = map(int, input().split())
        X[i] = x
        X_inv[N + 1 - i] = C - x
        V[i] = v
        V_inv[N + 1 - i] = v
    V_sum = to_cumsum(V)
    V_inv_sum = to_cumsum(V_inv)

    ans = 0
    for i in range(N + 1):
        for j in range(N - i + 1):
            v = V_sum[i] + V_inv_sum[j]
            x1 = X[i] + 2 * X_inv[j]
            x2 = 2 * X[i] + X_inv[j]
            ans = max(ans, v - min(x1, x2))
    print(ans)


if __name__ == '__main__':
    main()
