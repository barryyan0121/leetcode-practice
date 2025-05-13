/*
 * @lc app=leetcode.cn id=374 lang=java
 *
 * [374] 猜数字大小
 */

// @lc code=start
/**
 * Forward declaration of guess API.
 * 
 * @param num your guess
 * @return -1 if num is lower than the guess number
 *         1 if num is higher than the guess number
 *         otherwise return 0
 *         int guess(int num);
 */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int l = 1, r = n;
        while (l < r) {
            int m = (r - l) / 2 + l;
            int result = guess(m);
            if (result == -1) {
                r = m - 1;
            } else if (result == 1) {
                l = m + 1;
            } else {
                return m;
            }
        }
        return l;
    }
}
// @lc code=end
