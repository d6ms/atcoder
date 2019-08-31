#include <bits/stdc++.h>

using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, t) for (int i = (s); i < (int)(t); i++)


template<typename T>
vector<T> subvector(vector<T> const &v, int m, int n) {
    auto first = v.cbegin() + m;
    auto last = v.cbegin() + n;
    vector<T> vec(first, last);
    return vec;
}

template<typename T>
vector<vector<T>> combinations(vector<T> &it, int r) {
    vector<vector<T>> comb;
    int n = it.size();
    if (r > n)
        return comb;
    vector<int> indices(r);
    rep(i, r) indices[i] = i;
    vector<T> sub0(r);
    rep(k, r)sub0[k] = it[indices[k]];
    comb.emplace_back(sub0);
    while (true) {
        bool flg = false;
        for (int i = r - 1; i >= 0; i--) {
            if (indices[i] != i + n - r) {
                indices[i]++;
                rep2(j, i + 1, r)indices[j] = indices[j - 1] + 1;
                vector<T> sub(r);
                rep(k, r)sub[k] = it[indices[k]];
                comb.emplace_back(sub);
                flg = true;
                break;
            }
        }
        if (!flg)
            return comb;
    }
}

/**
* 階乗を事前計算した配列を作成します。
* @param n [0, n]の配列を作成します
* @return [0, n]の配列
*/
vector<long long> create_factorial(int n) {
    vector<long long> f(n);
    for (int i = 0; i < n + 1; i++) {
        if (i == 0 || i == 1) {
            f[i] = 1;
        } else {
            f[i] = f[i - 1] * i;
        }
    }
    return f;
}