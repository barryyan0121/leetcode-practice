/*
 * @lc app=leetcode.cn id=461 lang=java
 *
 * [461] 汉明距离
 */

// @lc code=start
class Solution {
    public int hammingDistance(int x, int y) {
        int s = x ^ y, count = 0;
        while (s != 0) {
            s &= (s - 1);
            count++;
        }
        return count;
    }
}
// @lc code=end
