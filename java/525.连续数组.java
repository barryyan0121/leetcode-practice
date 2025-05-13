import java.util.*;
/*
 * @lc app=leetcode.cn id=525 lang=java
 *
 * [525] 连续数组
 */

// @lc code=start
class Solution {
    public int findMaxLength(int[] nums) {
        int m = nums.length, res = 0;
        if (m < 2) {
            return res;
        }
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        map.put(0, -1);
        int counter = 0;
        for (int i = 0; i < m; i++) {
            counter += (nums[i] == 1) ? 1 : -1;
            if (map.containsKey(counter)) {
                int prevIndex = map.get(counter);
                res = Math.max(res, i - prevIndex);
            } else {
                map.put(counter, i);
            }
        }
        return res;
    }
}
// @lc code=end
