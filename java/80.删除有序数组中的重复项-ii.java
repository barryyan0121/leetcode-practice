/*
 * @lc app=leetcode.cn id=80 lang=java
 *
 * [80] 删除有序数组中的重复项 II
 */

// @lc code=start
class Solution {
    public int removeDuplicates(int[] nums) {
        int slow = 0, fast = 0, n = nums.length, count = 0;
        while (fast < n) {
            if (nums[slow] != nums[fast]) {
                nums[++slow] = nums[fast];
            } else if (slow < fast && count < 2) {
                nums[++slow] = nums[fast];
            }
            fast++;
            count++;
            if (fast < n && nums[fast] != nums[fast - 1]) {
                count = 0;
            }
        }
        return slow + 1;
    }
}
// @lc code=end
