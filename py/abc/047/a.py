def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))
MOD = 10 ** 9 + 7


a, b, c = MI()
if a + b == c or b + c == a or c + a == b:
    print('Yes')
else:
    print('No')
