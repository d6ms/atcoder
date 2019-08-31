#include <bits/stdc++.h>

using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, t) for (int i = (s); i < (int)(t); i++)
typedef long long ll;
const ll mod = 1e9 + 7;

int main() {
    int H, W;
    cin >> H >> W;
    vector<string> m(H);
    rep(i, H) {
        cin >> m[i];
    }

    vector<string> ans(H, "");
    vector<int> DH{-1, 0, 1};
    vector<int> DW{-1, 0, 1};
    rep(i, H) {
        rep(j, W) {
            if (m[i][j] == '#') {
                ans[i] += '#';
                continue;
            }
            int cnt = 0;
            for (int &dh: DH) {
                for (int &dw: DW) {
                    if (dh == 0 && dw == 0) {
                        continue;
                    }
                    if (i + dh < 0 || i + dh >= H || j + dw < 0 || j + dw >= W) {
                        continue;
                    }
                    if (m[i + dh][j + dw] == '#') {
                        cnt++;
                    }
                }
            }
            ans[i] += to_string(cnt);
        }
    }
    rep(i, H) {
        cout << ans[i] << endl;
    }

}