import java.util.LinkedList;

import java.util.*;
/*
 * @lc app=leetcode.cn id=216 lang=java
 *
 * [216] 组合总和 III
 */

// @lc code=start
class Solution {
    int k, n;

    public List<List<Integer>> combinationSum3(int k, int n) {
        this.k = k;
        this.n = n;
        backtrack(1, 0);
        return res;
    }

    List<List<Integer>> res = new LinkedList<>();
    LinkedList<Integer> track = new LinkedList<>();

    void backtrack(int start, int sum) {
        if (track.size() == k && sum == n) {
            res.add(new LinkedList<>(track));
            return;
        }

        for (int i = start; i < 10; i++) {
            sum += i;
            track.addLast(i);
            backtrack(i + 1, sum);
            sum -= i;
            track.removeLast();
        }
    }
}
// @lc code=end
