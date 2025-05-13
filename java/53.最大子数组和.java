/*
 * @lc app=leetcode.cn id=53 lang=java
 *
 * [53] 最大子数组和
 */

// @lc code=start
class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        if (n == 0)
            return 0;
        int sum = nums[0], max = nums[0];
        for (int i = 1; i < n; i++) {
            sum = Math.max(sum + nums[i], nums[i]);
            max = Math.max(max, sum);
        }
        return max;
    }
}
// @lc code=end
