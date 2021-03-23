#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        int x = click[0], y = click[1];
        if (board[x][y] == 'M') {
            board[x][y] = 'X';
        } else {
            dfs(board, x, y);
        }

        return board;
    }

    void dfs(vector<vector<char>>& board, int i, int j) {
        // 递归终止条件：判断空地 (i, j) 周围是否有雷，若有，则将该位置修改为雷数，终止该路径的搜索。
        int cnt = 0;
        for (int k = 0; k < 8; ++k) {
            int x = i + dx[k];
            int y = j + dy[k];
            if (x < 0 || x >= board.size() || y < 0 || y >= board[0].size()) {
                continue;
            }
            if (board[x][y] == 'M') {
                ++cnt;
            }
        }

        if (cnt > 0) {
            board[i][j] = (char)('0'+cnt);
            return;
        } else {
            board[i][j] = 'B';
        }

        for (int k = 0; k < 8; ++k) {
            int x = i + dx[k];
            int y = j + dy[k];

            if (x < 0 || x >= board.size() || y < 0 || y >= board[0].size() || board[x][y] != 'E') {
                continue;
            }

            dfs(board, x, y);
        }
    }

private:
    vector<int> dx = {-1, -1, -1, 0, 1, 1, 1, 0};
    vector<int> dy = {-1, 0, 1, 1, 1, 0, -1, -1};
};