#include <bits/stdc++.h>
#include <boost/range/irange.hpp>

using namespace std;
using boost::irange;
typedef long long ll;
const ll mod = 1e9 + 7;

int main() {
    string S;
    cin >> S;
    for (char c: "abcdefghijklmnopqrstuvwxyz"s) {
        if (S.find(c) == -1) {
            cout << c << endl;
            exit(0);
        }
    }
    cout << "None"s << endl;
    return 0;
}