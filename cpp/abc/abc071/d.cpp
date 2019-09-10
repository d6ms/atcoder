#include <bits/stdc++.h>
#include <boost/range/irange.hpp>

using namespace std;
using boost::irange;
typedef long long ll;
const ll mod = 1e9 + 7;

int main() {
    int N;
    cin >> N;
    string S0;
    string S1;
    cin >> S0 >> S1;

    ll ans = 1;
    if (S0[0] == S1[0]) {
        ans *= 3;
    } else {
        ans *= 6;
    }
    for (int i: irange(1, N)) {
        if (S0[i - 1] == S1[i - 1]) {
            ans = ans * 2 % mod;
        } else {
            if (S0[i - 1] == S0[i] && S1[i - 1] == S1[i])
                continue;
            if (S0[i] == S1[i]) {
                continue;
            } else {
                ans = ans * 3 % mod;
            }
        }
    }
    cout << ans << endl;
    return 0;
}