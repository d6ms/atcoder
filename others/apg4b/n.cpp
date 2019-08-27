#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, t) for (int i = (s); i < (int)(t); i++)

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    rep(i, N) {
        cin >> A.at(i);
    }
    int avg = accumulate(A.begin(), A.end(), 0) / A.size();
    rep(i, N) {
        cout << abs(A.at(i) - avg) << endl;
    }
}
