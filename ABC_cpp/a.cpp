#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> score;
    for (int i = 0; i < N; i++) {
        cin >> score[i];
    }
    // int avg;
    // for (int i = 0; i < N; i++) {
    //     avg += score[i];
    // }
    // avg /= N;
    cout << score[1] << endl;
    // cout << avg << endl;
    // for (int i = 0; i < score.size(); i++) {
    //     cout << abs(avg - score.at(i)) << endl;
    // }
}