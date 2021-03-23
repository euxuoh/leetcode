#include <bits/stdc++.h>

using namespace std;


std::vector<int> fa;
void init(int N) {
	fa.resize(N);
	for (int i = 0; i < N; i++) {
		fa[i] = i;
	}
}

int find(int x) {
	int r = x;
	while(fa[r] != r) {
		r = fa[r];
	}
	while(fa[x] != x) {
		int t = fa[x];
		fa[x] = r;
		x = t;
	}
	return x;
}

bool merge(int u, int v) {
	int ru = find(u);
	int rv = find(v);
    if (ru == rv) {
        return false;
    }
	fa[ru] = rv;
    return true;
}

class Solution {
public:
    int findCircleNum(vector<vector<int>>& M) {
        int N = M.size();
        init(N);
        int anw = N;
        for (int i = 0; i < N; i++) {
            for (int j = i+1; j < N; j++) {
                if (M[i][j] && merge(i, j)) {
                    anw --;
                }
            }
        }
        return anw;
    }
};
