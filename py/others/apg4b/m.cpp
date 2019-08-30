#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, t) for (int i = (s); i < (int)(t); i++)

int main() {
    string S;
    getline(cin, S);
    int v = 1;
    char op;
    rep2(i, 1, S.size()) {
        if (i % 2 == 0) {
            int num = 1;
            if (op == '+') {
                v += num;
            } else if (op == '-') {
                v -= num;
            }
        } else {
            op = S.at(i);
        }
    }
    cout << v << endl;
}
