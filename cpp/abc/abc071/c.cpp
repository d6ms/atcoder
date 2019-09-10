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
    for (int i: irange(0, N))
        cin >> A[i];

    sort(A.begin(), A.end());
    ll ans = 1;
    int cnt = 0;
    int hikae = -1;
    for (int i = N - 1; i >= 0; i--) {
        if (hikae == -1) {
            hikae = A[i];
        } else if (hikae == A[i]) {
            ans *= A[i];
            hikae = -1;
            cnt++;
            if (cnt == 2) {
                cout << ans << endl;
                exit(0);
            }
        } else {
            hikae = A[i];
        }
    }
    cout << 0 << endl;
    return 0;
}