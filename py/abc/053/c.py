x = int(input())

ans = (x // 11) * 2
amari = x % 11

if amari > 0:
    ans += 1
    amari -= 6

if amari > 0:
    ans += 1
    amari -= 5
print(ans)
