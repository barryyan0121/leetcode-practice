import java.util.HashSet;

/*
 * @lc app=leetcode.cn id=645 lang=java
 *
 * [645] 错误的集合
 */

// @lc code=start
class Solution {
    public int[] findErrorNums(int[] nums) {
        int dup = -1;
        for (int i = 0; i < nums.length; i++) {
            int index = Math.abs(nums[i]) - 1;
            if (nums[index] < 0) {
                dup = Math.abs(nums[i]);
            } else {
                nums[index] *= -1;
            }
        }
        int missing = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                missing = i + 1;
            }
        }
        return new int[] { dup, missing };

        // int sum = 0;
        // int n = nums.length;
        // int n1 = 0, n2 = 0;
        // HashSet<Integer> set = new HashSet<>();
        // for (int i : nums) {
        // sum += i;
        // if (set.contains(i)) {
        // n1 = i;
        // } else {
        // set.add(i);
        // }
        // }
        // int origin = (n + 1) * n / 2;
        // int diff = origin - sum;
        // n2 = n1 + diff;
        // return new int[] { n1, n2 };

    }
}
// @lc code=end
