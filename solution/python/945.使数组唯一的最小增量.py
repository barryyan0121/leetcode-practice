#
# @lc app=leetcode.cn id=945 lang=python3
#
# [945] 使数组唯一的最小增量
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        answer = 0
        next_value = 0
        for number in sorted(nums):
            next_value = max(next_value, number)
            answer += next_value - number
            next_value += 1
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minIncrementForUnique, ([1, 2, 2],), 1),
        (solution.minIncrementForUnique, ([3, 2, 1, 2, 1, 7],), 6),
        (solution.minIncrementForUnique, ([0, 0, 0],), 3),
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
