#
# @lc app=leetcode.cn id=3895 lang=python3
#
# [3895] 统计数字出现次数
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def countDigitOccurrences(self, nums: List[int], digit: int) -> int:
        target = str(digit)
        return sum(str(num).count(target) for num in nums)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.countDigitOccurrences, ([12, 54, 32, 22], 2), 4),
        (solution.countDigitOccurrences, ([1, 34, 7], 9), 0),
        (solution.countDigitOccurrences, ([100, 1010, 10], 0), 5),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: args = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: args = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
