#include <bits/stdc++.h>
using namespace std;

int main() {
    int x, a, b;
    cin >> x >> a >> b;
    int v = x + 1;
    cout << v << endl;
    v *= a + b;
    cout << v << endl;
    v *= v;
    cout << v << endl;
    cout << v - 1 << endl;
}
