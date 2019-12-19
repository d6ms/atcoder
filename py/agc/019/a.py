from decimal import Decimal, getcontext
getcontext().prec = 32

Q, H, S, D = map(int, input().split())
q = Decimal(Q * 4)
h = Decimal(H * 2)
s = Decimal(S)
d = Decimal(D / 2)

arr = [(q, Q, Decimal(0.25)), (h, H, Decimal(0.5)), (s, S, Decimal(1.0)), (d, D, Decimal(2.0))]
arr.sort()

N = int(input())

ans = 0
while N > 0:
    for _, cost, quantity in arr:
        if N >= quantity:
            ans += (N // quantity) * cost
            N -= (N // quantity) * quantity
print(int(ans))