N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

A.sort()
F.sort(reverse=True)


def shugyou_count(X):
    # 目標スコアをXとしたときの必要修行回数を求める
    count = 0
    for a, f in zip(A, F):
        count += max(0, a - X // f)
    return count


# 二分探索で達成可能な最小値を見つける
l = -1
r = max(A) * max(F)
while l + 1 < r:
    X = (l + r) // 2
    if shugyou_count(X) <= K:
        r = X
    else:
        l = X
print(r)

