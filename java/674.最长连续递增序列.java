/*
 * @lc app=leetcode.cn id=674 lang=java
 *
 * [674] 最长连续递增序列
 */

// @lc code=start
class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int n = nums.length, result = 1;
        int prev = 1, curr = 1;
        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1]) {
                curr = prev + 1;
            } else {
                curr = 1;
            }
            prev = curr;
            result = Math.max(result, curr);
        }
        return result;
    }
}
// @lc code=end
