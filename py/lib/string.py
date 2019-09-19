def lcp_array(S):
    """
    LCP array (文字列の各インデックスについて「SとS[i: len(S) - 1]の最長共通接頭辞の長さ」を計算した配列)
    を Z-algorithm を用いて O(|S|) で計算します。
    e.g.
    'aaabaaaab' => [9, 2 ,1 ,0 ,3 ,4 ,2 ,1 ,0]
    """
    A = [-1 for _ in range(len(S))]
    A[0] = len(S)
    i = 1
    j = 0
    while i < len(S):
        while i + j < len(S) and S[j] == S[i + j]:
            j += 1
        A[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i + k < len(S) and k + A[k] < j:
            A[i + k] = A[k]
            k += 1
        i += k
        j -= k
    return A