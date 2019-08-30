// 1問だけTLEになってしまう
#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, t) for (int i = (s); i < (int)(t); i++)
typedef pair<int, int> pii;

int main() {
    int N, Q;
    cin >> N >> Q;
    vector<pii> event(2 * N);
    rep (i, N) {
        int S, T, X;
        cin >> S >> T >> X;
        event[2 * i] = make_pair(S - X, X);
        event[2 * i + 1] = make_pair(T - X, - 1 * X);
    }
    sort(event.begin(), event.end(), less<>());
    vector<int> D(Q);
    rep (i, Q) cin >> D[i];

    int i = 0;
    unordered_set<int> stop;
    for (int &d: D) {
        while (i < event.size()) {
            pii p = event[i];
            int t = p.first;
            int X = p.second;
            if (t > d) {
                break;
            }
            if (X > 0) {
                stop.insert(X);
            } else {
                stop.erase(-1 * X);
            }
            i++;
        }
        if (stop.empty()) {
            cout << -1 << endl;
        } else {
            auto min_e = min_element(stop.begin(), stop.end());
            cout << *min_e << endl;
        }

    }

}
