A, B = map(int, input().split())
if B == 1:
    print(0)
    exit(0)

cnt = 1
n = A
while n < B:
    n += A - 1
    cnt += 1
print(cnt)