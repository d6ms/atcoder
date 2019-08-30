#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, t) for (int i = (s); i < (int)(t); i++)

int main() {
    int N, S;
    cin >> N >> S;
    vector<int> A(N), P(N);
    rep(i, N) cin >> A.at(i);
    rep(i, N) cin >> P.at(i);

    int cnt = 0;
    rep(i, N) {
        rep(j, N) {
            if (A[i] + P[j] == S) {
                cnt++;
            }
        }
    }
    cout << cnt << endl;
}
