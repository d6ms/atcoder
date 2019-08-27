N = int(input())

num = N
fx = 0
while num > 0:
    fx += num % 10
    num //= 10

if N % fx == 0:
    print('Yes')
else:
    print('No')
