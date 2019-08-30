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

print(nums)


# 要素の和のうち最大のものを求めるので累積和を計算して高速化する
cumsum = [nums[0]]
for i in range(1, len(nums)):
    cumsum.append(cumsum[i - 1] + nums[i])

print(cumsum)

# 0, 2, 4,...番目から始まる2K + 1要素の和で最大のものを求める
l = 0
ans = 0
while l < len(cumsum):
    r = l + (2 * K) + 1
    if r >= len(cumsum):
        r = len(cumsum) - 1
    ans = max(ans, cumsum[r] - cumsum[l])
    l += 2
print(ans)