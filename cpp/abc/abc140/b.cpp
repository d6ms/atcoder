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
    for (int i: irange(0, N)) cin >> A[i];
    vector<int> B(N + 1);
    for (int i: irange(1, N + 1)) cin >> B[i];
    vector<int> C(N);
    for (int i: irange(1, N)) cin >> C[i];

    int ans = 0;
    for (int i: irange(0, N)) {
        ans += B[A[i]];
        if (i > 0 && A[i] == A[i - 1] + 1) {
            ans += C[A[i] - 1];
        }
    }
    cout << ans << endl;

    return 0;
}