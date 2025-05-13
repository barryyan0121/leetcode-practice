/*
 * @lc app=leetcode.cn id=724 lang=java
 *
 * [724] 寻找数组的中心下标
 */

// @lc code=start
class Solution {
    public int pivotIndex(int[] nums) {
        int n = nums.length;
        int[] preSum = new int[n + 1];
        preSum[0] = 0;
        for (int i = 1; i <= n; i++) {
            preSum[i] = preSum[i - 1] + nums[i - 1];
        }
        for (int i = 1; i <= n; i++) {
            int left = preSum[i - 1] - preSum[0];
            int right = preSum[n] - preSum[i];
            if (left == right) {
                return i - 1;
            }
        }
        return -1;
    }
}
// @lc code=end
