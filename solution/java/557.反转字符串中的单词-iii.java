/*
 * @lc app=leetcode.cn id=557 lang=java
 *
 * [557] 反转字符串中的单词 III
 */

// @lc code=start
class Solution {
    public String reverseWords(String s) {
        int i = 0, j = 0;
        StringBuilder sb = new StringBuilder();
        while (j < s.length()) {
            char c = s.charAt(j);
            if (c == ' ') {
                sb.append(reverse(s.substring(i, j))).append(' ');
                i = j + 1;
            }
            j++;
        }
        sb.append(reverse(s.substring(i, j)));
        return sb.toString();
    }

    public StringBuilder reverse(String s) {
        StringBuilder sb = new StringBuilder("");
        for (int i = s.length() - 1; i >= 0; i--) {
            sb.append(s.charAt(i));
        }
        return sb;
    }
}
// @lc code=end
