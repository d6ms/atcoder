N = int(input())

L_2 = 2
L_1 = 1

if N == 1:
    print(1)
    exit(0)

i = 1
while i < N:
    L = L_1 + L_2
    L_2 = L_1
    L_1 = L
    i += 1
print(L)
