def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))


N = I()
A = LMI()

for a in A:
    if a % 2 == 0:
        if a % 3 != 0 and a % 5 != 0:
            print('DENIED')
            exit(0)
print('APPROVED')
