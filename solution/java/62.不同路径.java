/*
 * @lc app=leetcode.cn id=62 lang=java
 *
 * [62] 不同路径
 */

// @lc code=start
class Solution {
    int[][] memo;

    public int uniquePaths(int m, int n) {
        memo = new int[m][n];
        return dp(m - 1, n - 1);
    }

    int dp(int i, int j) {
        if (i == 0 && j == 0)
            return 1;
        if (i < 0 || j < 0)
            return 0;
        if (memo[i][j] > 0)
            return memo[i][j];

        memo[i][j] = dp(i - 1, j) + dp(i, j - 1);
        return memo[i][j];
    }
}
// @lc code=end
