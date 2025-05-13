import java.util.*;

/*
 * @lc app=leetcode.cn id=18 lang=java
 *
 * [18] 四数之和
 */

// @lc code=start
class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        return nSum(nums, 4, 0, target);
    }

    List<List<Integer>> nSum(int[] nums, int n, int start, long target) {

        int sz = nums.length;
        List<List<Integer>> res = new LinkedList<>();
        if (n < 2 || sz < n)
            return res;
        if (n == 2) {
            int lo = start, hi = sz - 1;
            while (lo < hi) {
                int nMin = nums[lo] + nums[lo + 1];
                if (nMin > target) {
                    break;
                }
                int nMax = nums[hi] + nums[hi - 1];
                if (nMax < target) {
                    break;
                }

                long sum = nums[lo] + nums[hi];
                int left = nums[lo], right = nums[hi];
                if (sum < target) {
                    while (lo < hi && nums[lo] == left)
                        lo++;
                } else if (sum > target) {
                    while (lo < hi && nums[hi] == right)
                        hi--;
                } else {
                    res.add(new LinkedList<Integer>(Arrays.asList(left, right)));
                    while (lo < hi && nums[lo] == left)
                        lo++;
                    while (lo < hi && nums[hi] == right)
                        hi--;
                }
            }
        } else {
            for (int i = start; i <= sz - n; i++) {
                List<List<Integer>> sub = nSum(nums, n - 1, i + 1, target - nums[i]);
                for (List<Integer> arr : sub) {
                    arr.add(nums[i]);
                    res.add(arr);
                }
                while (i <= sz - n - 1 && nums[i] == nums[i + 1])
                    i++;
            }
        }
        return res;
    }
}
// @lc code=end
