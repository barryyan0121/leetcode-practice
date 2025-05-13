/*
 * @lc app=leetcode.cn id=657 lang=java
 *
 * [657] 机器人能否返回原点
 */

// @lc code=start
class Solution {
    public boolean judgeCircle(String moves) {
        int x = 0, y = 0;
        char[] arr = moves.toCharArray();
        for (char c : arr) {
            if (c == 'R') {
                x++;
            } else if (c == 'L') {
                x--;
            } else if (c == 'U') {
                y++;
            } else {
                y--;
            }
        }
        return x == 0 && y == 0;
    }
}
// @lc code=end
