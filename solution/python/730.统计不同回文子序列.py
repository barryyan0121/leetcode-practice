#
# @lc app=leetcode.cn id=730 lang=python3
#
# [730] 统计不同回文子序列
#


# @lc code=start
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        mod = 10**9 + 7
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                if s[left] != s[right]:
                    dp[left][right] = (
                        dp[left + 1][right]
                        + dp[left][right - 1]
                        - dp[left + 1][right - 1]
                    ) % mod
                    continue
                inner_left, inner_right = left + 1, right - 1
                while inner_left <= inner_right and s[inner_left] != s[left]:
                    inner_left += 1
                while inner_left <= inner_right and s[inner_right] != s[left]:
                    inner_right -= 1
                if inner_left > inner_right:
                    value = 2 * dp[left + 1][right - 1] + 2
                elif inner_left == inner_right:
                    value = 2 * dp[left + 1][right - 1] + 1
                else:
                    value = (
                        2 * dp[left + 1][right - 1]
                        - dp[inner_left + 1][inner_right - 1]
                    )
                dp[left][right] = value % mod
        return dp[0][n - 1]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert solution.countPalindromicSubsequences("bccb") == 6
    assert solution.countPalindromicSubsequences("aaa") == 3
