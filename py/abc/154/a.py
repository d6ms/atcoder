def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))


S, T = input().split()
A, B = MI()
U = input()
if U == S:
    A -= 1
elif U == T:
    B -= 1
print(A, B)
