/*
 * @lc app=leetcode.cn id=171 lang=java
 *
 * [171] Excel 表列序号
 */

// @lc code=start
class Solution {
    public int titleToNumber(String columnTitle) {
        int sum = 0;
        char arr[] = columnTitle.toCharArray();
        for (int i = 0; i < arr.length; i++) {
            int number = arr[i] - 'A' + 1;
            sum += Math.pow(26, arr.length - i - 1) * number;
        }
        return sum;
    }
}
// @lc code=end
