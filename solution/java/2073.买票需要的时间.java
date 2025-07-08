/*
 * @lc app=leetcode.cn id=2073 lang=java
 *
 * [2073] 买票需要的时间
 */

// @lc code=start
class Solution {
    public int timeRequiredToBuy(int[] tickets, int k) {
        int res = 0;
        for (int i = 0; i < tickets.length; i++) {
            if (i <= k) {
                res += Math.min(tickets[k], tickets[i]);
            } else {
                res += Math.min(tickets[k] - 1, tickets[i]);
            }
        }
        return res;
    }
}
// @lc code=end
