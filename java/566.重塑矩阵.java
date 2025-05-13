/*
 * @lc app=leetcode.cn id=566 lang=java
 *
 * [566] 重塑矩阵
 */

// @lc code=start
class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int m = mat.length;
        int n = mat[0].length;
        if (m * n != r * c) {
            return mat;
        }
        int[][] ret = new int[r][c];
        int x = 0, y = 0;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                ret[i][j] = mat[x][y];
                if (y == n - 1) {
                    y = 0;
                    x++;
                } else {
                    y++;
                }
            }
        }
        return ret;
    }
}
// @lc code=end
