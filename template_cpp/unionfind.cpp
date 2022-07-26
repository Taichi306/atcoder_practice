#include<bits/stdc++.h>
using namespace std;

struct UnionFind {
    vector<int> rank, parents;

    UnionFind() {}
    UnionFind(int n) {
        rank.resize(n, 0);
        parents.resize(n, 0);
        for (int i = 0; i < n; i++) {
            makeTree(i);
        }
    }

    void makeTree(int x) {
        parents[x] = x;
        rank[x] = 0;
    }

    bool isSame(int x, int y) {
        x = findRoot(x);
        y = findRoot(y);
        if (x == y) return false;
        if (rank[x] > rank[y]) {
            parents[y] = x;
        } else {
            parents[x] = y;
            if (rank[x] == rank[y]) {
                rank[y]++;
            }
        }
    }

    int findRoot(int x) {
        if (x != parents[x]) {
            parents[x] = findRoot(parents[x]);
        }
        return parents[x];
    }
};