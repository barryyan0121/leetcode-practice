import java.util.ArrayList;

/*
 * @lc app=leetcode.cn id=448 lang=java
 *
 * [448] 找到所有数组中消失的数字
 */

// @lc code=start
class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        for (int n : nums) {
            int i = Math.abs(n) - 1;
            nums[i] = -Math.abs(nums[i]);
        }
        List<Integer> arr = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                arr.add(i + 1);
            }
        }
        return arr;
    }
}
// @lc code=end

// [4, 3, 2, 7, 8, 2, 3, 1]
// [4, 3, 2, -7, 8, 2, 3, 1]
// [4, 3, -2, -7, 8, 2, 3, 1]
// [4, -3, -2, -7, 8, 2, 3, 1]
// [4, -3, -2, -7, 8, 2, -3, 1]
// [4, -3, -2, -7, 8, 2, -3, -1]
// [4, -3, -2, -7, 8, 2, -3, -1]
// [4, -3, -2, -7, 8, 2, -3, -1]
// [-4, -3, -2, -7, 8, 2, -3, -1]
// 8 > 0 && 2 > 0 -> 5, 6
