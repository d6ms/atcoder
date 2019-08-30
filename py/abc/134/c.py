N = int(input())
A = [int(input()) for _ in range(N)]

max1 = 0
max2 = 0
for i in range(N):
    if max2 < A[i]:
        if A[i] > max1:
            max2 = max1
            max1 = A[i]
        else:
            max2 = A[i]

for i in range(N):
    if A[i] == max1:
        print(max2)
    else:
        print(max1)
