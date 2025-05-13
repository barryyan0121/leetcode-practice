/*
 * @lc app=leetcode.cn id=258 lang=java
 *
 * [258] 各位相加
 */

// @lc code=start
class Solution {
    public int addDigits(int num) {
        // while (num >= 10) {
        //     num = getSum(num);
        // }
        // return num;
        return (num - 1) % 9 + 1;
    }

    public int getSum(int num) {
        int sum = 0;
        while (num != 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}
// @lc code=end

