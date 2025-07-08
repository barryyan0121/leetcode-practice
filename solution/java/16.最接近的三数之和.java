import java.util.Arrays;

/*
 * @lc app=leetcode.cn id=16 lang=java
 *
 * [16] 最接近的三数之和
 */

// @lc code=start
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        if (nums.length < 3)
            return 0;
        Arrays.sort(nums);
        int delta = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length - 2; i++) {
            int sum = nums[i] + twoSumClosest(nums, i + 1, target - nums[i]);
            if (Math.abs(delta) > Math.abs(target - sum)) {
                delta = target - sum;
            }
        }
        return target - delta;

    }

    int twoSumClosest(int[] nums, int start, int target) {
        int lo = start, hi = nums.length - 1;
        int delta = Integer.MAX_VALUE;
        while (lo < hi) {
            int sum = nums[lo] + nums[hi];
            if (Math.abs(delta) > Math.abs(target - sum)) {
                delta = target - sum;
            }
            if (sum < target) {
                lo++;
            } else {
                hi--;
            }
        }
        return target - delta;
    }
}
// @lc code=end
