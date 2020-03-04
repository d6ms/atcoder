from decimal import Decimal, getcontext
getcontext().prec = 32

N = Decimal(int(input()))

if N % 2 == 1:
    print(0)
    exit(0)

ans = Decimal(0)
for i in range(1, 28):
    ans += (N // (Decimal(5) ** Decimal(i))) // Decimal(2)

print(ans)