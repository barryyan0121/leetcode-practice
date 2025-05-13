/*
 * @lc app=leetcode.cn id=401 lang=java
 *
 * [401] 二进制手表
 */

// @lc code=start
class Solution {
    public List<String> readBinaryWatch(int turnedOn) {
        List<String> ret = new ArrayList<>();
        for (int h = 0; h < 12; h++) {
            for (int m = 0; m < 60; m++) {
                if (Integer.bitCount(h) + Integer.bitCount(m) == turnedOn) {
                    ret.add(h + ":" + (m < 10 ? "0" : "") + m);
                }
            }
        }
        return ret;
    }
}
// @lc code=end
