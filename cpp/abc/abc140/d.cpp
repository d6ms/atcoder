#include <bits/stdc++.h>
#include <boost/range/irange.hpp>

using namespace std;
using boost::irange;
typedef long long ll;
const ll mod = 1e9 + 7;

int main() {
    int N, K;
    cin >> N >> K;
    string S;
    cin >> S;

    int h = 0;
    for (int i: irange(1, N)) {
        if (S[i] == S[i - 1]) h++;
    }
    cout << min(h + 2 * K, N - 1) << endl;

    return 0;
}