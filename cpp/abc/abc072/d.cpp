#include <bits/stdc++.h>
#include <boost/range/irange.hpp>

using namespace std;
using boost::irange;
typedef long long ll;
const ll mod = 1e9 + 7;

int main() {
    int N;
    cin >> N;
    vector<int> p(N);
    for (int i: irange(0, N)) {
        cin >> p[i];
    }

    int cnt = 0;
    for (int i: irange(0, N - 1)) {
        if (p[i] == i + 1) {
            swap(p[i], p[i + 1]);
            cnt++;
        }
    }
    if (p[N - 1] == N) {
        cnt++;
    }
    cout << cnt << endl;
    return 0;
}