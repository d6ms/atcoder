#include <bits/stdc++.h>

using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, t) for (int i = (s); i < (int)(t); i++)
typedef long long ll;
const ll mod = 1e9 + 7;

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

int main() {
    int N, K;
    cin >> N >> K;
    vector<pair<int, int>> XY(N);
    vector<int> X(N);
    vector<int> Y(N);
    rep(i, N) {
        int x, y;
        cin >> x >> y;
        XY[i] = make_pair(x, y);
        X[i] = x;
        Y[i] = y;
    }

    sort(X.begin(), X.end());
    sort(Y.begin(), Y.end());
    ll ans = LLONG_MAX;
    for (vector<int> &xsub: combinations(X, 2)) {
        for (vector<int> &ysub: combinations(Y, 2)) {
            int cnt = 0;
            for (pair<int, int> &p: XY) {
                int x = p.first;
                int y = p.second;
                if (xsub[0] <= x && x <= xsub[1] && ysub[0] <= y && y <= ysub[1]) {
                    cnt++;
                }
            }
            if (K <= cnt) {
                ans = min(ans, (ll)(xsub[1] - xsub[0]) * (ysub[1] - ysub[0]));
            }
        }
    }
    cout << ans << endl;
}