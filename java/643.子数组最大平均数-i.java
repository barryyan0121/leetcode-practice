/*
 * @lc app=leetcode.cn id=643 lang=java
 *
 * [643] 子数组最大平均数 I
 */

// @lc code=start
class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int sum = 0;
        for (int i = 0; i < k; i++) {
            sum += nums[i];
        }
        int result = sum;
        for (int i = k; i < nums.length; i++) {
            sum += nums[i] - nums[i - k];
            result = Math.max(result, sum);
        }
        return (double) result / k;
    }
}
// @lc code=end
