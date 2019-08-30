#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, t) for (int i = (s); i < (int)(t); i++)

int main() {
    int N, M;
    cin >> N >> M;
    vector<vector<char>> t(N, vector<char>(N, '-'));
    rep(_, M) {
        int A, B;
        cin >> A >> B;
        t[A - 1][B - 1] = 'o';
        t[B - 1][A - 1] = 'x';
    }
    rep(i, N) {
        int len = t[i].size();
        rep(j, len) {
            cout << t[i][j];
            if (j == len - 1) {
                cout << endl;
            } else {
                cout << " ";
            }
        }
    }
}
