/*
 * @lc app=leetcode.cn id=238 lang=java
 *
 * [238] 除自身以外数组的乘积
 */

// @lc code=start
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] prefix = new int[n], suffix = new int[n], res = new int[n];
        prefix[0] = nums[0];
        suffix[n - 1] = nums[n - 1];
        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] * nums[i];
            suffix[n - 1 - i] = suffix[n - i] * nums[n - 1 - i];
        }
        res[0] = suffix[1];
        res[n - 1] = prefix[n - 2];
        for (int i = 1; i < n - 1; i++) {
            res[i] = suffix[i + 1] * prefix[i - 1];
        }
        return res;

    }
}
// @lc code=end
