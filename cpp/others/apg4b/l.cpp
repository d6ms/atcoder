#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, t) for (int i = (s); i < (int)(t); i++)

int main() {
    int N, A;
    cin >> N >> A;
    bool error = false;
    rep(i, N) {
        string op;
        int B;
        cin >> op >> B;
        if (op == "+") {
            A += B;
        } else if (op == "-") {
            A -= B;
        } else if (op == "*") {
            A *= B;
        } else if (op == "/") {
            if (B == 0) {
                error = true;
                break;
            }
            A /= B;
        } else {
            error = true;
            break;
        }
        cout << i + 1 << ":" << A << endl;
    }
    if (error) {
        cout << "error" << endl;
    }
}
