/*
 * @lc app=leetcode.cn id=168 lang=java
 *
 * [168] Excel表列名称
 */

// @lc code=start
class Solution {
    public String convertToTitle(int columnNumber) {
        StringBuilder s = new StringBuilder("");
        int value = 0;
        while (columnNumber-- != 0) {
            value = columnNumber % 26;
            s.append((char) ('A' + value));
            columnNumber /= 26;
        }
        return s.reverse().toString();
    }
}
// @lc code=end
