def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))


W, H = MI()

if W % 16 == 0 and H % 9 == 0:
    print('16:9')
else:
    print('4:3')
