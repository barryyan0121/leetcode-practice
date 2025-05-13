/*
 * @lc app=leetcode.cn id=482 lang=java
 *
 * [482] 密钥格式化
 */

// @lc code=start
class Solution {
    public String licenseKeyFormatting(String s, int k) {
        char[] arr = s.toUpperCase().toCharArray();
        StringBuilder str = new StringBuilder("");
        int count = 0;
        for (int i = arr.length - 1; i >= 0; i--) {
            char c = arr[i];
            if (c != '-') {
                count++;
                str.append(c);
                if (count == k && i != 0) {
                    str.append('-');
                    count = 0;
                }
            }
        }
        if (str.length() > 0 && str.charAt(str.length() - 1) == '-') {
            str.deleteCharAt(str.length() - 1);
        }
        return str.reverse().toString();
    }
}
// @lc code=end
