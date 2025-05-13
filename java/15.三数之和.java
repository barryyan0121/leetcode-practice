import java.util.*;

/*
 * @lc app=leetcode.cn id=15 lang=java
 *
 * [15] 三数之和
 */

// @lc code=start
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        if (nums.length < 3) {
            return res;
        }
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            ArrayList<ArrayList<Integer>> tuples = twoSum(nums, i + 1, -nums[i]);
            for (ArrayList<Integer> tuple: tuples) {
                tuple.add(nums[i]);
                res.add(tuple);
            }
            while (i < nums.length - 1 && nums[i] == nums[i + 1]) i++;
        }
        return res;
    }

    public ArrayList<ArrayList<Integer>> twoSum(int[] nums, int start, int target) {
        int lo = start, hi = nums.length - 1;
        ArrayList<ArrayList<Integer>> res = new ArrayList<>();
        while (lo < hi) {
            int sum = nums[lo] + nums[hi];
            int left = nums[lo], right = nums[hi];
            if (sum < target) {
                while (lo < hi && nums[lo] == left) lo++;
            } else if (sum > target) {
                while (lo < hi && nums[hi] == right) hi--;
            } else {
                res.add(new ArrayList<>(List.of(left, right)));
                while (lo < hi && nums[lo] == left) lo++;
                while (lo < hi && nums[hi] == right) hi--;
            }
        }
        return res;
    }
}
// @lc code=end

