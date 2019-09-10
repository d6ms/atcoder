#include <bits/stdc++.h>
#include <boost/range/irange.hpp>

using namespace std;
using boost::irange;
typedef long long ll;
const ll mod = 1e9 + 7;

int main() {
    int x, a, b;
    cin >> x >> a >> b;
    if (abs(x - a) > abs(x - b)) {
        cout << "B"s << endl;
    } else {
        cout << "A"s << endl;
    }
    return 0;
}