#include <bits/stdc++.h>
#include <boost/range/irange.hpp>

using namespace std;
using boost::irange;
typedef long long ll;
const ll mod = 1e9 + 7;

long long GCD(long long a, long long b) {
    if (b == 0) return a;
    else return GCD(b, a % b);
}

long long LCM(long long a, long long b) {
    long long g = GCD(a, b);
    return a / g * b;
}

vector<pair<int, int>> factorize(int n) {
    int b = 2;
    vector<pair<int, int>> fct(0);
    while (b * b <= n) {
        int cnt = 0;
        while (n % b == 0) {
            cnt += 1;
            n /= b;
            if (cnt > 0) {
                fct.emplace_back(b, cnt);
                b += 1;
            }
        }
        if (n > 1)
            fct.emplace_back(n, 1);
    }
    return fct;
}
int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i: irange(0, N)) cin >> A[i];

    ll l = A[0];
    for (int i: irange(0, N))
        l = LCM(l, A[i]);

    ll ans = 0;
    for (int i: irange(0, N)) {
        ans += l / A[i] % mod;
        ans %= mod;
    }
    cout << ans << endl;
    return 0;
}