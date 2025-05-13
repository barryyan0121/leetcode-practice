/*
 * @lc app=leetcode.cn id=66 lang=java
 *
 * [66] 加一
 */

// @lc code=start
class Solution {
    public int[] plusOne(int[] digits) {
        for (int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] != 9) {
                digits[i]++;
                for (int j = i + 1; j < digits.length; j++) {
                    digits[j] = 0;
                }
                return digits;
            }
        }
        int[] ret = new int[digits.length + 1];
        ret[0] = 1;
        return ret;
    }
}
// @lc code=end

