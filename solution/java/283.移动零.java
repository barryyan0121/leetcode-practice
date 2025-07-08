/*
 * @lc app=leetcode.cn id=283 lang=java
 *
 * [283] 移动零
 */

// @lc code=start
class Solution {
    public void moveZeroes(int[] nums) {
        int fast = 0, slow = 0, n = nums.length;
        while (fast < n) {
            if (nums[slow] == 0) {
                if (nums[fast] != 0) {
                    nums[slow] = nums[fast];
                    nums[fast] = 0;
                    slow++;
                }
            } else {
                slow++;
            }
            fast++;
        }
    }
}
// @lc code=end
