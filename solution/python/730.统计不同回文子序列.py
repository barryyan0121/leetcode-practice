#
# @lc app=leetcode.cn id=730 lang=python3
#
# [730] 统计不同回文子序列
#

import os
import sys


# @lc code=start
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        mod = 1_000_000_007
        length = len(s)
        dp = [[0] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1

        for size in range(2, length + 1):
            for left in range(length - size + 1):
                right = left + size - 1
                if s[left] != s[right]:
                    dp[left][right] = (
                        dp[left + 1][right]
                        + dp[left][right - 1]
                        - dp[left + 1][right - 1]
                    )
                    continue
                low, high = left + 1, right - 1
                while low <= high and s[low] != s[left]:
                    low += 1
                while low <= high and s[high] != s[left]:
                    high -= 1
                dp[left][right] = 2 * dp[left + 1][right - 1]
                if low > high:
                    dp[left][right] += 2
                elif low == high:
                    dp[left][right] += 1
                else:
                    dp[left][right] -= dp[low + 1][high - 1]
                dp[left][right] %= mod
        return dp[0][-1]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.countPalindromicSubsequences, ("bccb",), 6),
        (solution.countPalindromicSubsequences, ("abcd",), 4),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
