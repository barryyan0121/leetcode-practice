/*
 * @lc app=leetcode.cn id=64 lang=java
 *
 * [64] 最小路径和
 */

// @lc code=start
class Solution {
    int[][] grid, memo;
    int m, n;

    public int minPathSum(int[][] grid) {
        this.grid = grid;
        this.m = grid.length;
        this.n = grid[0].length;
        this.memo = new int[m][n];
        for (int[] row : memo)
            Arrays.fill(row, -1);

        return dp(m - 1, n - 1);
    }

    int dp(int i, int j) {
        if (i == 0 && j == 0) {
            return grid[0][0];
        }
        if (i < 0 || j < 0)
            return Integer.MAX_VALUE;
        if (memo[i][j] != -1)
            return memo[i][j];
        memo[i][j] = Math.min(dp(i - 1, j), dp(i, j - 1)) + grid[i][j];
        return memo[i][j];
    }
}
// @lc code=end
