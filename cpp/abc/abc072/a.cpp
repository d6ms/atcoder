#include <bits/stdc++.h>
#include <boost/range/irange.hpp>

using namespace std;
using boost::irange;
typedef long long ll;
const ll mod = 1e9 + 7;

int main() {
    int X, t;
    cin >> X >> t;
    cout << max(0, X - t) << endl;
    return 0;
}