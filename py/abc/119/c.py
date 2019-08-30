# 解けなかったので解説を見た
# 竹の総数が8と少なく、それぞれの竹の利用パターンもA/B/Cの材料とするor使わないの4種類なので全列挙する
# 可能なパターンを全列挙するのであればdfsを用いて、消費MPの最小値を考えれば良い

N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]


def dfs(i, a_len, b_len, c_len):
    # 探索の葉に達したときは残りの延長・短縮の工数を調べて返す
    if i == N:
        if a_len == 0 or b_len == 0 or c_len == 0:  # 0を延長して竹を作ることはできない
            return float('inf')
        else:
            return abs(a_len - A) + abs(b_len - B) + abs(c_len - C) - 30  # 1本目の連結は本来工数ゼロなので最後に引いておく

    br1 = dfs(i + 1, a_len + L[i], b_len, c_len) + 10  # L[i]をaに連結する場合
    br2 = dfs(i + 1, a_len, b_len + L[i], c_len) + 10  # L[i]をbに連結する場合
    br3 = dfs(i + 1, a_len, b_len, c_len + L[i]) + 10  # L[i]をcに連結する場合
    br4 = dfs(i + 1, a_len, b_len, c_len)  # L[i]を使わない場合

    return min(br1, br2, br3, br4)


print(dfs(0, 0, 0, 0))
