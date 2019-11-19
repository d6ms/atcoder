MOD = 10 ** 9 + 7

X, Y = map(int, input().split())

a = (2 * X - Y) / 3
if not a.is_integer():
    print(0)
    exit(0)
a = int(a)

ans = 1
for i in range(2, X - a + 1):
    ans = ans * i
    if i <= a:
        ans = ans / i
    if i <= X - 2 * a:
        ans = ans / i
    ans = ans % MOD
print(ans)