#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, t) for (int i = (s); i < (int)(t); i++)

int main() {
    int N, M;
    cin >> N >> M;
    vector<vector<int>> nl(N + 1);
    rep(i, M) {
        int X, Y, Z;
        cin >> X >> Y >> Z;
        nl[X].push_back(Y);
        nl[Y].push_back(X);
    }

    int ans = 0;
    unordered_set<int> seen;
    stack<int> st;
    rep2(i, 1, N + 1) {
        if (seen.find(i) == seen.end()) {
            ans++;
            st.push(i);
            while (st.size() > 0) {
                int v = st.top();
                st.pop();
                for (int &next_v : nl[v]) {
                    seen.insert(v);
                    if (seen.find(next_v) == seen.end()) {
                        st.push(next_v);
                    }
                }
            }
        }
    }
    cout << ans << endl;
}
