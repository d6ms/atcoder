def to_cumsum(arr, pad=True):
    """
    1次元配列を累積和の1次元配列に変換する
    pad: 先頭に0の項を作る場合はTrue
    """
    cumsum = 0
    padding = 1 if pad else 0
    new = [0] * (len(arr) + padding)
    for i, e in enumerate(arr):
        cumsum += e
        new[i + padding] = cumsum
    return new


N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)


def pairs_to_achieve(X):

    pass

# 上位Mペアを求めたい
# => Xを動かして増える幸福度がX以上となるペアを探す (Xを増やせばペア数は減る)
# => Mペア以上がX以上を達成できるギリギリまでXを増やす
# => 上位Mペアが残る
l = -1
r = N * N
while l + 1 < r:
    X = (l + r) // 2
    # 幸福度Xを達成するために上位何ペアの和を取ればよいか考える
    if pairs_to_achieve(X) >= M:
        r = X
    else:
        l = X

# r := 増える幸福度がr以上となるペアがM個ある
print(r)