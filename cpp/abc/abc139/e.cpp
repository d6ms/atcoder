#include <bits/stdc++.h>
#include <boost/range/irange.hpp>

using namespace std;
using boost::irange;
typedef long long ll;
const ll mod = 1e9 + 7;

int main() {
    int N;
    cin >> N;
    vector<deque<int>> A(N + 1, deque<int>());
    for (int i: irange(1, N + 1)) {
        for (int j: irange(0, N - 1)) {
            int val;
            cin >> val;
            A[i].push_back(val);
        }
    }

    vector<int> day(N + 1, 1);
    int empty_queues = 0;
    while (empty_queues < N) {
        bool matched = false;
        for (int i: irange(1, N + 1)) {
            int competitor = A[i].front();
            if (A[competitor].front() == i) {
                matched = true;
                A[i].pop_front();
                A[competitor].pop_front();
                int date = max(day[i], day[competitor]) + 1;
                day[i] = date;
                day[competitor] = date;
                if (A[i].empty()) {
                    empty_queues++;
                }
                if (A[competitor].empty()) {
                    empty_queues++;
                }
            }
        }
        if (!matched) {
            cout << -1 << endl;
            exit(0);
        }
    }
    int ans = 0;
    for (int i: irange(1, N + 1)) {
        ans = max(ans, day[i]);
    }
    cout << ans - 1 << endl;
}