import java.util.*;
/*
 * @lc app=leetcode.cn id=322 lang=java
 *
 * [322] 零钱兑换
 */

// @lc code=start
class Solution {

    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;

        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (i >= coin) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }
        return (dp[amount] > amount) ? -1 : dp[amount];
    }

    int[] memo;

    public int coinChangeFunction(int[] coins, int amount) {
        memo = new int[amount + 1];
        Arrays.fill(memo, -666);
        return dp(coins, amount);

    }

    int dp(int[] coins, int amount) {
        if (amount == 0)
            return 0;
        if (amount < 0)
            return -1;
        if (memo[amount] != -666)
            return memo[amount];
        int res = Integer.MAX_VALUE;
        for (int coin : coins) {
            int sub = dp(coins, amount - coin);
            if (sub == -1)
                continue;
            res = Math.min(res, sub + 1);
        }
        memo[amount] = (res == Integer.MAX_VALUE) ? -1 : res;
        return memo[amount];
    }
}
// @lc code=end
