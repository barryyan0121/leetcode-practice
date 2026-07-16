#
# @lc app=leetcode.cn id=1014 lang=python3
#
# [1014] 最佳观光组合
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best_left = values[0]
        result = 0
        for index in range(1, len(values)):
            result = max(result, best_left + values[index] - index)
            best_left = max(best_left, values[index] + index)
        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maxScoreSightseeingPair, ([8, 1, 5, 2, 6],), 11),
        (solution.maxScoreSightseeingPair, ([1, 2],), 2),
        (solution.maxScoreSightseeingPair, ([7, 7, 7],), 13),
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
