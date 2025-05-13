import java.util.*;

/*
 * @lc app=leetcode.cn id=22 lang=java
 *
 * [22] 括号生成
 */

// @lc code=start
class Solution {
    public List<String> generateParenthesis(int n) {
        if (n == 0)
            return res;
        backtrack("", n, n);
        return res;
    }

    List<String> res = new ArrayList<>();

    void backtrack(String curStr, int left, int right) {
        if (left == 0 && right == 0) {
            res.add(curStr);
            return;
        }
        if (left > right)
            return;
        if (left > 0) {
            backtrack(curStr + "(", left - 1, right);
        }
        if (right > 0) {
            backtrack(curStr + ")", left, right - 1);
        }
    }
}
// @lc code=end
