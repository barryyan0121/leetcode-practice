/*
 * @lc app=leetcode.cn id=1021 lang=java
 *
 * [1021] 删除最外层的括号
 */

// @lc code=start
class Solution {
    public String removeOuterParentheses(String s) {
        int level = 0;
        StringBuffer res = new StringBuffer();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == ')') {
                level--;
            }
            if (level > 0) {
                res.append(c);
            }
            if (c == '(') {
                level++;
            }
        }
        return res.toString();
    }

}
// @lc code=end
