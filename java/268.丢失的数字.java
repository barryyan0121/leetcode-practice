/*
 * @lc app=leetcode.cn id=268 lang=java
 *
 * [268] 丢失的数字
 */

// @lc code=start
class Solution {
    public int missingNumber(int[] nums) {
        int sum = 0;
        int n = nums.length;
        for (int i : nums) {
            sum += i;
        }
        int curr = (1 + n) * n / 2;
        return curr - sum;
    }
}
// @lc code=end
