/*
 * @lc app=leetcode.cn id=59 lang=java
 *
 * [59] 螺旋矩阵 II
 */

// @lc code=start
class Solution {
    public int[][] generateMatrix(int n) {
        int[][] res = new int[n][n];
        int left = 0, right = n - 1, top = 0, bottom = n - 1;
        int i = 0;
        while (left <= right && top <= bottom) {
            for (int column = left; column <= right; column++) {
                res[top][column] = ++i;
            }
            for (int row = top + 1; row <= bottom; row++) {
                res[row][right] = ++i;
            }
            if (left < right && top < bottom) {
                for (int column = right - 1; column > left; column--) {
                    res[bottom][column] = ++i;
                }
                for (int row = bottom; row > top; row--) {
                    res[row][left] = ++i;
                }
            }
            left++;
            right--;
            top++;
            bottom--;
        }
        return res;
    }
}
// @lc code=end
