#include <bits/stdc++.h>
#include <boost/range/irange.hpp>

using namespace std;
using boost::irange;
typedef long long ll;
const ll mod = 1e9 + 7;

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i: irange(0, N)) {
        cin >> A[i];
    }

    unordered_map<int, int> d;
    for (int i: irange(0, N)) {
        vector<int> cand{A[i] - 1, A[i], A[i] + 1};
        for (int &c: cand) {
            if (d[c]) {
                d[c]++;
            } else {
                d[c] = 1;
            }
        }
    }
    int ans = 0;
    for (auto kv: d) {
        ans = max(ans, kv.second);
    }
    cout << ans << endl;
    return 0;
}