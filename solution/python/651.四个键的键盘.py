#
# @lc app=leetcode.cn id=651 lang=python3
#
# [651] 四个键的键盘
#


# @lc code=start
class Solution:
    def maxA(self, n: int) -> int:
        dp = list(range(n + 1))
        for i in range(4, n + 1):
            dp[i] = max(dp[i - 1] + 1, *(dp[j] * (i - j - 1) for j in range(1, i - 2)))
        return dp[n]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxA(3) == 3
    assert solution.maxA(7) == 9
