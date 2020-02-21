from bisect import bisect_right

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

# X := 計算結果のある要素
# 計算結果の小さい方からK番目の数 := X以下の計算結果がK個以上あるような最小のX


def X_ikano_kosu(X):
    cnt = 0
    for a in A:
        # a * b <= X  <=>  b <= X // a
        cnt += bisect_right(B, X // a)
    return cnt


l = A[0] * B[0]
r = A[-1] * B[-1]
while l + 1 < r:
    X = (l + r) // 2
    # Xを決めた時、X以下の数はK個以上あるか？
    if X_ikano_kosu(X) >= K:
        r = X
    else:
        l = X
if X_ikano_kosu(l) >= K:
    print(l)
else:
    print(r)
