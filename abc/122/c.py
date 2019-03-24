# コンテスト時LTE
# アルゴリズムの計算量は良かったが、1回あたりの処理が遅かった
# 「AC」を発見したインデックスでなく、「AC」の数の累積和を保持しておけば計算が速かった

def solve(N, Q, S, L_R):
    memo = [None] * N
    cumsum = 0
    for i in range(len(S) - 1):
        memo[i] = cumsum
        if S[i] == "A" and S[i + 1] == "C":
            cumsum += 1
    memo[N - 1] = cumsum
    for l, r in L_R:
        print(memo[r - 1] - memo[l - 1])


N, Q = map(int, input().split())
S = input()
L_R = [tuple(map(int, input().split())) for _ in range(Q)]
solve(N, Q, S, L_R)