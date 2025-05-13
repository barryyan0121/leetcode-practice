/*
 * @lc app=leetcode.cn id=520 lang=java
 *
 * [520] 检测大写字母
 */

// @lc code=start
class Solution {
    public boolean detectCapitalUse(String word) {
        char[] arr = word.toCharArray();
        int number = 0;

        for (int i = 1; i < arr.length; i++) {
            char c = arr[i];
            if (Character.isUpperCase(c)) {
                number++;
            }
        }
        if (Character.isUpperCase(arr[0])) {
            if (number == arr.length - 1) {
                return true;
            }
        }
        if (number == 0) {
            return true;
        }
        return false;
    }
}
// @lc code=end
