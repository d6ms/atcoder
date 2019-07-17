def sub753(K, lst):
    if K == 1:
        return ['3', '5', '7']
    ans = [pre + suf for suf in sub753(K - 1, lst) for pre in '357']
    lst.extend(ans)
    return ans


N = int(input())

lst = list()
sub753(10, lst)

cnt = 0
for num in lst:
    if '3' in num and '5' in num and '7' in num and int(num) <= N:
        cnt += 1
print(cnt)
