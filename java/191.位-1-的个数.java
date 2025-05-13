/*
 * @lc app=leetcode.cn id=191 lang=java
 *
 * [191] 位1的个数
 */

// @lc code=start
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int sum = 0;
        while (n != 0) {
            // sum += n & 1;
            // n >>>= 1;
            n = n & (n - 1);
            sum++;
        }
        return sum;
    }
}
// @lc code=end
