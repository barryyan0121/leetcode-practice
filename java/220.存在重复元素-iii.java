import java.util.HashMap;
/*
 * @lc app=leetcode.cn id=220 lang=java
 *
 * [220] 存在重复元素 III
 */
import java.util.TreeSet;

// @lc code=start
class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        TreeSet<Long> set = new TreeSet<>();
        for (int i = 0; i < nums.length; i++) {
            Long u = nums[i] * 1L;
            Long l = set.floor(u);
            Long r = set.ceiling(u);
            if (l != null && u - l <= t)
                return true;
            if (r != null && r - u <= t)
                return true;
            set.add(u);
            if (i >= k)
                set.remove(nums[i - k] * 1L);
        }
        return false;
    }
}
// @lc code=end
