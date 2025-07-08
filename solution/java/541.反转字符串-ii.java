/*
 * @lc app=leetcode.cn id=541 lang=java
 *
 * [541] 反转字符串 II
 */

// @lc code=start
class Solution {
    public String reverseStr(String s, int k) {
        char[] c = s.toCharArray();
        for (int i = 0; i < c.length; i += 2 * k) {
            reverse(c, i, Math.min(i + k, c.length) - 1);
        }
        return new String(c);
    }

    public void reverse(char[] arr, int left, int right) {
        while (left < right) {
            char temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
    }
}
// @lc code=end
