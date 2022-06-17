#include <bits/stdc++.h>
// #define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

int main() {
    int N, A;
    cin >> N >> A;

    for (int i=0; i < N; i++) {
        string op;
        int B;
        cin >> op >> B;
        if (op == "+") {
            A += B;
        } else if (op == "-") {
            A -= B;
        } else if (op == "*") {
            A *= B;
        } else {
            if (B == 0) {
                cout << "error" << endl;
                break;
            }
            else {
                A /= B;
            }
        }
        cout << i+1 << ":" << A << endl;
    }
}