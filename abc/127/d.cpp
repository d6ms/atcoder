#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, t) for (int i = (s); i < (int)(t); i++)

int main() {
    int N, M;
    cin >> N >> M;
    priority_queue<int, vector<int>, greater<int>> A;
    rep(i, N) {
        int A_i;
        cin >> A_i;
        A.push(A_i);
    }
    vector<pair<int, int>> BC(M);
    rep(i, M) {
        int B, C;
        cin >> B >> C;
        BC[i] = make_pair(B, C);
    }

    sort(BC.begin(), BC.end(), [](pair<int, int> x, pair<int, int> y) -> int {
        return x.second > y.second;
    });
    for (pair<int, int> &p: BC) {
        for (int i = 0; i < p.first; i ++) {
            if (A.top() < p.second) {
                A.pop();
                A.push(p.second);
            } else{
                break;
            }
        }
    }

    long long sum = 0;
    while (!A.empty()) {
        sum += A.top();
        A.pop();
    }
    cout << sum << endl;
}
