/*
 * @lc app=leetcode.cn id=63 lang=java
 *
 * [63] 不同路径 II
 */

// @lc code=start
class Solution {
    int[][] memo, obstacleGrid;

    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length, n = obstacleGrid[0].length;
        memo = new int[m][n];
        this.obstacleGrid = obstacleGrid;
        return dp(m - 1, n - 1);
    }

    int dp(int i, int j) {
        if (i < 0 || j < 0 || obstacleGrid[i][j] == 1)
            return 0;
        if (i == 0 && j == 0)
            return 1;
        if (memo[i][j] > 0)
            return memo[i][j];

        memo[i][j] = dp(i - 1, j) + dp(i, j - 1);
        return memo[i][j];
    }
}
// @lc code=end
