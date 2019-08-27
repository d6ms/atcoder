#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, t) for (int i = (s); i < (int)(t); i++)

int main() {
    vector<int> A(5);
    rep(i, 5) cin >> A.at(i);
    rep2(i, 1, 5) {
        if (A[i] == A[i - 1]) {
            cout << "YES" << endl;
            exit(0);
        }
    }
    cout << "NO" << endl;
}
