def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))


A = input()

if len(A) > 1:
    print(A[:-1])
elif A[0] != 'a':
    print(chr(ord(A[0]) - 1))
else:
    print(-1)