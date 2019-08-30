// WAなのでだめ
#include <bits/stdc++.h>

using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, t) for (int i = (s); i < (int)(t); i++)
typedef long long ll;
const ll mod = 1e9 + 7;

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

int main() {
    int N, K;
    cin >> N >> K;
    vector<ll> f = create_factorial(K);
    vector<vector<int>> nl(N + 1);
    rep(i, N - 1) {
        int a, b;
        cin >> a >> b;
        nl[a].push_back(b);
        nl[b].push_back(a);
    }

    ll ans = K;
    deque<pair<int, int>> q;
    q.emplace_back(make_pair(1, -1));
    while (!q.empty()) {
        int v = q.front().first;
        int p = q.front().second;
        q.pop_front();
        int children = 0;
        for (int &next_v: nl[v]) {
            if (next_v != p) {
                children++;
                q.emplace_back(make_pair(next_v, v));
            }
        }
        if (children > 0) {
            int n = v == 1 ? K - 1 : K - 2;
            int r = children;
            ll perm = f[n] / f[n - r];
            ans = (ans * perm) % mod;
        }
    }
    cout << ans << endl;
}