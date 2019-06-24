N, K = map(int, input().split())
A = list(map(int, input().split()))

r = 0
l = 0
cnt = 0
# 尺取り法でカウントする(O(N)のはずだけどTLEする)
while r < N:
    # 右に1つ進めても総和がKに達しない場合は進める
    if sum(A[l: r + 1]) < K:
        r += 1
        continue
    # 右を進めて総和がKに達した場合はカウントして左を一つ進める
    if r != l:
        cnt += N - r
        l += 1
    # 右と左が同じ位置にいる場合は右も一緒に進める
    else:
        cnt += N - r
        l += 1
        r += 1

print(cnt)
