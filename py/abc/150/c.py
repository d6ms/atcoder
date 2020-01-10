N = int(input())
P = ''.join(input().split())
Q = ''.join(input().split())

from itertools import permutations

arr = list()
for i in permutations(list(range(1, N + 1)), N):
    arr.append(''.join([str(x) for x in i]))

print(abs(arr.index(Q) - arr.index(P)))