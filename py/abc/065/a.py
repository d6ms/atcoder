def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))

X, A, B = MI()
if A >= B:
    print('delicious')
elif B - A <= X:
    print('safe')
else:
    print('dangerous')