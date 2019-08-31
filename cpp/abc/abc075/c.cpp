#include <bits/stdc++.h>

using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, t) for (int i = (s); i < (int)(t); i++)
typedef long long ll;
const ll mod = 1e9 + 7;

int main() {
    int N, M;
    cin >> N >> M;
    vector<vector<int>> nl(N + 1);
    vector<pair<int, int>> edges(M);
    rep(i, M) {
        int a, b;
        cin >> a >> b;
        nl[a].emplace_back(b);
        nl[b].emplace_back(a);
        edges[i] = make_pair(a, b);
    }

    int cnt = 0;
    for (pair<int, int> &edge: edges) {
        stack<int> st;
        unordered_set<int> seen;
        st.push(1);
        while (!st.empty()) {
            int v = st.top();
            st.pop();
            seen.insert(v);
            for (int &next_v: nl[v]) {
                if ((v == edge.first && next_v == edge.second) || (v == edge.second && next_v == edge.first)) {
                    continue;
                } else if (seen.find(next_v) == seen.end()) {
                    st.push(next_v);
                }
            }
        }
        if (seen.size() < N) {
            cnt++;
        }
    }
    cout << cnt << endl;
}