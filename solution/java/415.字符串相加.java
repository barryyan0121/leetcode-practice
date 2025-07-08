/*
 * @lc app=leetcode.cn id=415 lang=java
 *
 * [415] 字符串相加
 */

// @lc code=start
class Solution {
    public String addStrings(String num1, String num2) {
        StringBuilder res = new StringBuilder("");
        int i = num1.length() - 1;
        int j = num2.length() - 1;
        int carry = 0, digit = 0;
        while (i >= 0 || j >= 0) {
            int n1 = i >= 0 ? num1.charAt(i) - '0' : 0;
            int n2 = j >= 0 ? num2.charAt(j) - '0' : 0;
            digit = carry + n1 + n2;
            carry = digit / 10;
            digit %= 10;
            res.append(digit);
            i--;
            j--;
        }
        if (carry == 1)
            res.append(1);
        return res.reverse().toString();
    }
}
// @lc code=end
