S = input()
T = input()

l = len(T)
min_cnt = float('inf')
for i in range(len(S) - l + 1):
    s = S[i: i + l]
    cnt = 0
    for j in range(len(s)):
        if s[j] != T[j]:
            cnt += 1
    min_cnt = min(min_cnt, cnt)
print(min_cnt)
