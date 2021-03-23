#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int rows = grid.size();
        if (rows == 0) return 0;
        int cols = grid[0].size();
        if (cols == 0) return 0;

        int num_island = 0;
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (grid[i][j] == '1') {
                    ++num_island;
                    dfs(grid, i, j);
                }
            }
        }

        return num_island;
    }

    void dfs(vector<vector<char>>& grid, int i, int j) {
        int nr = grid.size();
        int nc = grid[0].size();

        if (i < 0 || i >= nr || j < 0 || j >= nc || grid[i][j] != '1') {
            return;
        }

        grid[i][j] = '2';

        dfs(grid, i-1, j);
        dfs(grid, i+1, j);
        dfs(grid, i, j-1);
        dfs(grid, i, j+1);
    } 
};