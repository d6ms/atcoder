from fractions import gcd


# 最小公倍数はGCDを使って算出できる
def lcm(a, b):
    return a * b // gcd(a, b)


A, B, C, D = map(int, input().split())

# B以下の整数のうち、CでもDでも割り切れないものの個数
cnt_B = B - (B // C + B // D) + B // lcm(C, D)

# A - 1以下の整数のうち、CでもDでも割り切れないものの個数
A_1 = A - 1
cnt_A = A_1 - (A_1 // C + A_1 // D) + A_1 // lcm(C, D)

print(cnt_B - cnt_A)
