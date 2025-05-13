import java.util.HashMap;

/*
 * @lc app=leetcode.cn id=389 lang=java
 *
 * [389] 找不同
 */

// @lc code=start
class Solution {
    public char findTheDifference(String s, String t) {
        int ret = 0;
        for (char ch : s.toCharArray()) {
            ret ^= ch;
        }
        for (char ch : t.toCharArray()) {
            ret ^= ch;
        }
        return (char) ret;
    }
}
// @lc code=end
