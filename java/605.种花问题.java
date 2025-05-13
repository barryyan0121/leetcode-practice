/*
 * @lc app=leetcode.cn id=605 lang=java
 *
 * [605] 种花问题
 */

// @lc code=start
class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        if (flowerbed.length == 0) {
            return n == 0;
        }
        int zeros = 1;
        int flower = 0;
        for (int bed : flowerbed) {
            if (bed == 0) {
                zeros++;
            } else {
                flower += (zeros - 1) / 2;
                if (flower >= n)
                    return true;
                zeros = 0;
            }
        }
        zeros++;
        flower += (zeros - 1) / 2;
        return flower >= n;
    }
}
// @lc code=end
