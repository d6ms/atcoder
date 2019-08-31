#include <bits/stdc++.h>

using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, t) for (int i = (s); i < (int)(t); i++)
typedef long long ll;
const ll mod = 1e9 + 7;

int main() {
    int A, B, C;
    cin >> A >> B >> C;
    if (A == B) {
        cout << C << endl;
    } else if (B == C) {
        cout << A << endl;
    } else {
        cout << B << endl;
    }
}