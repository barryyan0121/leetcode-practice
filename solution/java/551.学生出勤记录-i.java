/*
 * @lc app=leetcode.cn id=551 lang=java
 *
 * [551] 学生出勤记录 I
 */

// @lc code=start
class Solution {
    public boolean checkRecord(String s) {
        int absent = 0, late = 0, max_late = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'A') {
                absent++;
                late = 0;
            } else if (c == 'L') {
                late++;
                max_late = Math.max(max_late, late);
            } else {
                late = 0;
            }
        }
        if (absent < 2 && max_late < 3) {
            return true;
        }
        return false;
    }
}
// @lc code=end
