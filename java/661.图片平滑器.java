/*
 * @lc app=leetcode.cn id=661 lang=java
 *
 * [661] 图片平滑器
 */

// @lc code=start
class Solution {
    public int[][] imageSmoother(int[][] img) {
        int m = img.length;
        int n = img[0].length;
        int[][] ret = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int num = 0, sum = 0;
                for (int x = i - 1; x <= i + 1; x++) {
                    for (int y = j - 1; y <= j + 1; y++) {
                        if (x >= 0 && y >= 0 && x < m && y < n) {
                            sum += img[x][y];
                            num++;
                        }
                    }
                }
                ret[i][j] = sum / num;
            }
        }
        return ret;
    }
}
// @lc code=end
