/*
 * @lc app=leetcode.cn id=130 lang=java
 *
 * [130] 被围绕的区域
 */

// @lc code=start
class Solution {
    char[][] board;

    public void solve(char[][] board) {
        this.board = board;
        int m = board.length, n = board[0].length;
        for (int j = 0; j < n; j++) {
            dfs(0, j);
            dfs(m - 1, j);
        }
        for (int i = 0; i < m; i++) {
            dfs(i, 0);
            dfs(i, n - 1);
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'A') {
                    board[i][j] = 'O';
                } else if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
            }
        }
    }

    void dfs(int i, int j) {
        if (i < 0 || j < 0 || i >= board.length || j >= board[0].length) {
            return;
        }
        if (board[i][j] != 'O') {
            return;
        }
        board[i][j] = 'A';
        dfs(i - 1, j);
        dfs(i + 1, j);
        dfs(i, j + 1);
        dfs(i, j - 1);
    }
}
// @lc code=end
