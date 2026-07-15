#
# @lc app=leetcode.cn id=728 lang=python3
#
# [728] 自除数
#

import os
import sys
from typing import *


# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [
            number
            for number in range(left, right + 1)
            if "0" not in str(number)
            and all(number % int(digit) == 0 for digit in str(number))
        ]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.selfDividingNumbers,
            (1, 22),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22],
        ),
        (solution.selfDividingNumbers, (47, 85), [48, 55, 66, 77]),
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
