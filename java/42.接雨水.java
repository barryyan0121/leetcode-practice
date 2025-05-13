/*
 * @lc app=leetcode.cn id=42 lang=java
 *
 * [42] 接雨水
 */

// @lc code=start
class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int res = 0;
        int[] l = new int[n];
        int[] r = new int[n];
        l[0] = height[0];
        r[n - 1] = height[n - 1];
        for (int i = 1; i < n; i++) {
            l[i] = Math.max(height[i], l[i - 1]);
        }
        for (int i = n - 2; i >= 0; i--) {
            r[i] = Math.max(height[i], r[i + 1]);
        }
        for (int i = 1; i < n - 1; i++) {
            res += Math.min(l[i], r[i]) - height[i];
        }
        return res;
    }
}
// @lc code=end
