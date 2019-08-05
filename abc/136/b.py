N = int(input())

cnt = 0
for i in range(1, N + 1):
    if 10 <= i <= 99 or 1000 <= i <= 9999 or i == 100000:
        continue
    else:
        cnt += 1
print(cnt)