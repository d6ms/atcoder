from random import randint


class RollingHash(object):
    mod = 1 << 61 - 1
    base = randint(2, mod - 2)

    def __init__(self, s):
        """
        sに関するローリングハッシュを構築する O(|s|)
        cf. |s|<=5000 の構築で最大200ms程度
        """
        self.s = s
        self.pw = pw = [1] * (len(s) + 1)

        l = len(s)
        self.h = h = [0] * (l + 1)

        v = 0
        for i in range(l):
            h[i + 1] = v = (v * self.base + ord(s[i])) % self.mod
        v = 1
        for i in range(l):
            pw[i + 1] = v = v * self.base % self.mod

    def hash(self, l, r):
        """ s[l:r] のhash (rはexclusive) O(1) """
        return (self.h[r] - self.h[l] * self.pw[r - l]) % self.mod

    def contains(self, t):
        """
        sがtを含むか O(|s|-|t|)
        tはRollingHashオブジェクト
        """
        slen, tlen = len(self.s), len(t.s)
        if slen < tlen:
            return False
        th = t.hash(0, tlen)
        for i in range(slen - tlen + 1):
            if th == self.hash(i, i + tlen):
                return True
        return False

    def count(self, t):
        """
        s中に含まれるtの数をカウントする O(|s|-|t|)
        tはRollingHashオブジェクト
        """
        slen, tlen = len(self.s), len(t.s)
        if slen < tlen:
            return 0
        cnt = 0
        th = t.hash(0, tlen)
        for i in range(slen - tlen + 1):
            if th == self.hash(i, i + tlen):
                cnt += 1
        return cnt


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