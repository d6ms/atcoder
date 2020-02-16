t = int(input())
for _ in range(t):
    s = input()
    if '1' not in s:
        print(0)
        continue
    l = s.index('1')
    r = s.rindex('1')
    cnt = 0
    for i in range(l, r):
        if s[i] == '0':
            cnt += 1
    print(cnt)
