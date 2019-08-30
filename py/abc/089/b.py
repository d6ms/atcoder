N = int(input())
S = input().split()

size = len(set(S))
if size == 3:
    print('Three')
elif size == 4:
    print('Four')
