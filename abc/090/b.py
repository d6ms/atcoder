A, B = map(int, input().split())

cnt = 0
for num in range(A, B + 1):
    num = str(num)
    kaibun = True
    for i in range(len(num) // 2):
        if num[i] != num[-i - 1]:
            kaibun = False
            break
    if kaibun:
        cnt += 1
print(cnt)