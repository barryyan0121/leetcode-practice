import java.util.*;
/*
 * @lc app=leetcode.cn id=491 lang=java
 *
 * [491] 递增子序列
 */

// @lc code=start
class Solution {
    List<List<Integer>> ans = new ArrayList<List<Integer>>();
    List<Integer> temp = new ArrayList<Integer>();
    int[] nums;

    public List<List<Integer>> findSubsequences(int[] nums) {
        this.nums = nums;
        backtrack(0, Integer.MIN_VALUE);
        return ans;
    }

    void backtrack(int cur, int last) {
        if (cur == nums.length) {
            if (temp.size() >= 2) {
                ans.add(new ArrayList<Integer>(temp));
            }
            return;
        }
        if (nums[cur] >= last) {
            temp.add(nums[cur]);
            backtrack(cur + 1, nums[cur]);
            temp.remove(temp.size() - 1);
        }

        if (nums[cur] != last) {
            backtrack(cur + 1, last);
        }
    }
}
// @lc code=end
