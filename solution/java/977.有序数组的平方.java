/*
 * @lc app=leetcode.cn id=977 lang=java
 *
 * [977] 有序数组的平方
 */

// @lc code=start
class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int i = 0, j = n - 1;
        int p = n - 1;
        int[] res = new int[n];
        while (i <= j) {
            if (Math.abs(nums[i]) > Math.abs(nums[j])) {
                res[p--] = nums[i] * nums[i++];
            } else {
                res[p--] = nums[j] * nums[j--];
            }
        }
        return res;
    }
}
// @lc code=end
