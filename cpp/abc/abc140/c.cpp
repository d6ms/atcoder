#include <bits/stdc++.h>
#include <boost/range/irange.hpp>

using namespace std;
using boost::irange;
typedef long long ll;
const ll mod = 1e9 + 7;

int main() {
    int N;
    cin >> N;
    vector<int> B(N - 1);
    for (int i: irange(0, N - 1)) cin >> B[i];

    vector<int> A(N);
    for (int i: irange(0, N)) {
        if (i == 0) {
            A[i] = B[i];
        } else if (i == N - 1) {
            A[i] = B[i - 1];
        } else {
            A[i] = min(B[i - 1], B[i]);
        }
    }
    cout << accumulate(A.begin(), A.end(), 0) << endl;
    return 0;
}