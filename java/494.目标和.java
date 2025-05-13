import java.util.HashMap;

/*
 * @lc app=leetcode.cn id=494 lang=java
 *
 * [494] 目标和
 */

// @lc code=start
class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        return dp(nums, 0, target);
    }

    HashMap<String, Integer> memo = new HashMap<>();

    int dp(int[] nums, int i, int remain) {
        if (i == nums.length) {
            if (remain == 0)
                return 1;
            return 0;
        }
        String key = i + "," + remain;
        if (memo.containsKey(key)) {
            return memo.get(key);
        }
        int result = dp(nums, i + 1, remain - nums[i]) + dp(nums, i + 1, remain + nums[i]);
        memo.put(key, result);
        return result;
    }
}
// @lc code=end
