N = int(input())

n = N
S = 0
while True:
    S += n % 10
    new_n = n // 10
    if new_n == n:
        break
    else:
        n = new_n

if N % S == 0:
    print('Yes')
else:
    print('No')