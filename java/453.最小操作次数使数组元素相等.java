/*
 * @lc app=leetcode.cn id=453 lang=java
 *
 * [453] 最小操作次数使数组元素相等
 */

// @lc code=start
class Solution {
    public int minMoves(int[] nums) {
        int minNum = Arrays.stream(nums).min().getAsInt();
        int ret = 0;
        for (int num : nums) {
            ret += num - minNum;
        }
        return ret;
    }
}
// @lc code=end
