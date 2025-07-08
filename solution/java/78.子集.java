import java.util.*;
/*
 * @lc app=leetcode.cn id=78 lang=java
 *
 * [78] 子集
 */

// @lc code=start
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        backtrack(nums, 0);
        return res;
    }

    List<List<Integer>> res = new LinkedList<>();
    LinkedList<Integer> track = new LinkedList<>();

    void backtrack(int[] nums, int start) {

        res.add(new LinkedList<>(track));

        for (int i = start; i < nums.length; i++) {
            track.addLast(nums[i]);
            backtrack(nums, i + 1);
            track.removeLast();
        }
    }
}
// @lc code=end
