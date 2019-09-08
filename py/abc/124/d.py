def to_cumsum(arr):
    """
    1次元配列を累積和の1次元配列に変換する
    """
    cumsum = 0
    new = list()
    for e in arr:
        cumsum += e
        new.append(cumsum)
    return new


N, K = map(int, input().split())
S = input()

# 連続する1の数、連続する0の数を交互に並べた配列を計算
# 両端に1がない場合は"0個の1"があるものとして、必ず両端は1を示す要素にしておく

nums = list()
if S.startswith('0'):
    nums.append(0)

cnt = 0
cur = S[0]
for c in S:
    if c == cur:
        cnt += 1
    else:
        nums.append(cnt)
        cnt = 1
        cur = '1' if cur == '0' else '0'
nums.append(cnt)

if S.endswith('0'):
    nums.append(0)

# 要素の和のうち最大のものを求めるので累積和を計算して高速化する
cumsum = to_cumsum(nums)

# 0, 2, 4,...番目から始まる2K + 1要素の和で最大のものを求める
l = -1
ans = 0
while l < len(cumsum):
    r = l + (2 * K) + 1
    if r >= len(cumsum):
        r = len(cumsum) - 1
    if l == -1:
        ans = cumsum[r]
    else:
        ans = max(ans, cumsum[r] - cumsum[l])
    l += 2
print(ans)