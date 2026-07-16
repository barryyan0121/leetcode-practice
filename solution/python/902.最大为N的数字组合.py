#
# @lc app=leetcode.cn id=902 lang=python3
#
# [902] 最大为 N 的数字组合
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        limit = str(n)
        choices = len(digits)
        answer = sum(choices**length for length in range(1, len(limit)))
        for index, digit in enumerate(limit):
            remaining = len(limit) - index - 1
            answer += (
                sum(candidate < digit for candidate in digits) * choices**remaining
            )
            if digit not in digits:
                return answer
        return answer + 1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.atMostNGivenDigitSet, (["1", "3", "5", "7"], 100), 20),
        (solution.atMostNGivenDigitSet, (["1", "4", "9"], 1_000_000_000), 29523),
        (solution.atMostNGivenDigitSet, (["7"], 8), 1),
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
