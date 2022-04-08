MOD = 10 ** 9 + 7

N = int(input())

# 10 ** N - (|0 が存在しない| +  |9 が存在しない| - |0 も 9 も存在しない|)
ans = pow(10, N, MOD)
ans = (ans - pow(9, N, MOD) + MOD) % MOD
ans = (ans - pow(9, N, MOD) + MOD) % MOD
ans = (ans + pow(8, N, MOD)) % MOD
print(ans)
