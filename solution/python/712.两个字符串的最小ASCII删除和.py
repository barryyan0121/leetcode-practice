#
# @lc app=leetcode.cn id=712 lang=python3
#
# [712] 两个字符串的最小 ASCII 删除和
#

import os
import sys


# @lc code=start
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [sum(map(ord, s2[j:])) for j in range(len(s2) + 1)]
        for i in range(len(s1) - 1, -1, -1):
            previous = dp[-1]
            dp[-1] += ord(s1[i])
            for j in range(len(s2) - 1, -1, -1):
                old = dp[j]
                if s1[i] == s2[j]:
                    dp[j] = previous
                else:
                    dp[j] = min(ord(s1[i]) + old, ord(s2[j]) + dp[j + 1])
                previous = old
        return dp[0]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minimumDeleteSum, ("sea", "eat"), 231),
        (solution.minimumDeleteSum, ("delete", "leet"), 403),
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
