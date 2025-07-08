import java.util.LinkedList;

import java.util.*;
/*
 * @lc app=leetcode.cn id=46 lang=java
 *
 * [46] 全排列
 */

// @lc code=start
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        used = new boolean[nums.length];
        Arrays.fill(used, false);
        backtrack(nums);
        return res;
    }

    List<List<Integer>> res = new LinkedList<>();
    LinkedList<Integer> track = new LinkedList<>();
    boolean[] used;

    void backtrack(int[] nums) {
        if (track.size() == nums.length) {
            res.add(new LinkedList<>(track));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) {
                continue;
            }
            used[i] = true;
            track.addLast(nums[i]);
            backtrack(nums);
            used[i] = false;
            track.removeLast();
        }
    }
}
// @lc code=end
