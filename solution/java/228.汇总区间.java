import java.util.ArrayList;
import java.util.List;

/*
 * @lc app=leetcode.cn id=228 lang=java
 *
 * [228] 汇总区间
 */

// @lc code=start
class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> res = new ArrayList<>();
        int i = 0, n = nums.length;
        while (i < n) {
            int low = nums[i];
            while (i < n - 1 && nums[i] + 1 == nums[i + 1]) {
                i++;
            }
            int high = nums[i];
            StringBuilder s = new StringBuilder(Integer.toString(low));
            if (high > low) {
                s.append("->" + Integer.toString(high));
            }
            res.add(s.toString());
            i++;
        }
        return res;
    }
}
// @lc code=end
