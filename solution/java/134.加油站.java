/*
 * @lc app=leetcode.cn id=134 lang=java
 *
 * [134] 加油站
 */

// @lc code=start
class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length;
        int sum = 0, minSum = 0, start = 0;
        for (int i = 0; i < n; i++) {
            sum += gas[i] - cost[i];
            if (sum < minSum) {
                start = i + 1;
                minSum = sum;
            }
        }
        if (sum < 0) {
            return -1;
        }
        return start == n ? 0 : start;
    }
}
// @lc code=end
