/*
 * @lc app=leetcode.cn id=342 lang=java
 *
 * [342] 4的幂
 */

// @lc code=start
class Solution {
    public boolean isPowerOfFour(int n) {
        if ((n & (n - 1)) != 0 || n <= 0) {
            return false;
        }

        return n % 3 == 1;
    }
}
// @lc code=end
