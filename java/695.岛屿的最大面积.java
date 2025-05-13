/*
 * @lc app=leetcode.cn id=695 lang=java
 *
 * [695] 岛屿的最大面积
 */

// @lc code=start
class Solution {
    int[][] grid;

    public int maxAreaOfIsland(int[][] grid) {
        int res = Integer.MIN_VALUE;
        this.grid = grid;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    res = Math.max(res, dfs(i, j));
                }
            }
        }
        return res == Integer.MIN_VALUE ? 0 : res;
    }

    int dfs(int i, int j) {
        if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length) {
            return 0;
        }
        if (grid[i][j] == 0) {
            return 0;
        }
        grid[i][j] = 0;
        return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j + 1) + dfs(i, j - 1);
    }
}
// @lc code=end
