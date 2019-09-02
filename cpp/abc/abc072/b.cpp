#include <bits/stdc++.h>
#include <boost/range/irange.hpp>

using namespace std;
using boost::irange;
typedef long long ll;
const ll mod = 1e9 + 7;

int main() {
    string s;
    getline(cin, s);

    for (int i: irange(0, (int) s.size(), 2)) {
        cout << s[i];
    }
    cout << endl;
    return 0;
}