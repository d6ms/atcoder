#include <bits/stdc++.h>
using namespace std;

int main() {
    int pattern;
    cin >> pattern;
    if (pattern == 1) {
        int price, N;
        cin >> price >> N;
        cout << price * N << endl;
    } else if (pattern == 2) {
        string text;
        int price, N;
        cin >> text >> price >> N;
        cout << text + "!" << endl
             << N * price << endl;
    }
}
