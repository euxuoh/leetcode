#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // 哈希表存储每一行的每个数是否出现过，默认初始情况下，每一行每一个数都没有出现过
        int row[9][10] = {0};

        // 整个board有9行，第二维的维数10是为了让下标有9，和数独中的数字9对应
        // 存储每一列的每个数是否出现过，默认初始情况下，每一列的每一个数都没有出现过
        // 存储每一个box的每个数是否出现过，默认初始情况下，在每个box中，每个数都没有出现过。整个board有9个box
        int col[9][10] = {0};
        int box[9][10] = {0};

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                // 遍历到第i行第j列的那个数,我们要判断这个数在其所在的行有没有出现过
                // 同时判断这个数在其所在的列有没有出现过
                // 同时判断这个数在其所在的box中有没有出现过
                if (board[i][j] == '.') {
                    continue;
                }

                int curNumber = board[i][j] - '0';
                if (row[i][curNumber]) {
                    return false;
                }
                if (col[j][curNumber]) {
                    return false;
                }
                if (box[j/3 + (i/3)*3][curNumber]) {
                    return false;
                }

                // 之前都没出现过，现在出现了，就给它置为1，下次再遇见就能够直接返回false了
                row[i][curNumber] = 1;
                col[j][curNumber] = 1;
                box[j/3 + (i/3)*3][curNumber] = 1;
            }
        }
        return true;
    }
};
