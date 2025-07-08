/*
 * @lc app=leetcode.cn id=125 lang=java
 *
 * [125] 验证回文串
 */

// @lc code=start
class Solution {
    public boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;
        char[] arr = s.toLowerCase().toCharArray();
        while (i < j) {
            while (i < j && !Character.isLetterOrDigit(arr[i])) {
                i++;
            }
            while (i < j && !Character.isLetterOrDigit(arr[j])) {
                j--;
            }
            if (i < j && arr[i++] != arr[j--]) {
                return false;
            }
        }
        return true;
    }
}
// @lc code=end
