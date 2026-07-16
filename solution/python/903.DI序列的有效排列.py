#
# @lc app=leetcode.cn id=903 lang=python3
#
# [903] DI 序列的有效排列
#

import os
import sys


# @lc code=start
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        dp = [1]
        for relation in s:
            if relation == "I":
                next_dp = [0]
                for count in dp:
                    next_dp.append(next_dp[-1] + count)
            else:
                next_dp = [0] * (len(dp) + 1)
                for index in range(len(dp) - 1, -1, -1):
                    next_dp[index] = next_dp[index + 1] + dp[index]
            dp = [count % 1_000_000_007 for count in next_dp]
        return sum(dp) % 1_000_000_007


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numPermsDISequence, ("DID",), 5),
        (solution.numPermsDISequence, ("D",), 1),
        (solution.numPermsDISequence, ("III",), 1),
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
