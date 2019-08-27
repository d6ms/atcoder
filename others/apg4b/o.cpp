#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, t) for (int i = (s); i < (int)(t); i++)

int main() {
    int A, B, C;
    cin >> A >> B >> C;
    cout << max(max(A, B), C) - min(min(A, B), C) << endl;
}
