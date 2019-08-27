#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, t) for (int i = (s); i < (int)(t); i++)

int count(vector<int> &P, vector<int> &ans, int i, int cnt) {
    if (P.at(i) == -1) {
        ans.at(i) = cnt;
        return cnt;
    } else {
        cnt = count(P, ans, P.at(i), cnt + 1);
        ans.at(i) = cnt;
        return cnt;
    }
}

int main() {
    int N;
    cin >> N;
    vector<int> P(N, -1);
    rep2(i, 1, N - 1) {
        cin >> P.at(i);
    }
    vector<vector<int>> C(N);
    
}
