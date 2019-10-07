S = input()
K = int(input())

sumarr = list()
cnt = 1
for i in range(1, len(S)):
    if S[i] == S[i - 1]:
        cnt += 1
    else:
        sumarr.append(cnt)
        cnt = 1
sumarr.append(cnt)

if len(sumarr) == 1:
    print(int(len(S) * K / 2))
    exit(0)


def to_cnt(num):
    if num < 2:
        return 0
    else:
        return int(num / 2)


ans = 0
if S[0] == S[len(S) - 1]:
    ans += to_cnt(sumarr[0])
    ans += to_cnt(sumarr[len(sumarr) - 1])
    connection = to_cnt(sumarr[0] + sumarr[len(sumarr) - 1])
    cnt = sum(map(to_cnt, sumarr[1: len(sumarr) - 1]))
    ans += cnt * K
    ans += connection * (K - 1)
else:
    ans += sum(map(to_cnt, sumarr)) * K

print(ans)
