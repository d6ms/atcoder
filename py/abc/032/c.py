import numpy as np


def solve(N, K, S):
    # 0が含まれる場合はしゃくとり法で上手くいかない(総乗で0になるところまでは見切れない)ので分岐処理
    if 0 in S:
        return N

    answer = 0
    r = 0
    l = 0
    while r < N:
        # 右に1つ進めても条件を満たす場合は進める
        if np.prod(S[l: r + 1]) <= K:  # 総乗
            r += 1
            answer = max(answer, r - l)
            continue
        # 右に進めない場合は左を一つ進める
        if r != l:
            l += 1
        # 右と左が同じ位置にいる場合は右も一緒に進める
        else:
            l += 1
            r += 1
    return answer


N, K = map(int, input().split())
S = [int(input()) for _ in range(N)]
print(solve(N, K, S))
