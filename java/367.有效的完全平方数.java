/*
 * @lc app=leetcode.cn id=367 lang=java
 *
 * [367] 有效的完全平方数
 */

// @lc code=start
class Solution {
    public boolean isPerfectSquare(int num) {
        int low = 0, high = num, mid = 0;
        long square = 0;
        while (low <= high) {
            mid = (high - low) / 2 + low;
            square = (long) mid * mid;
            if (square < num) {
                low = mid + 1;
            } else if (square == num) {
                return true;
            } else {
                high = mid - 1;
            }
        }
        return false;
    }
}
// @lc code=end
