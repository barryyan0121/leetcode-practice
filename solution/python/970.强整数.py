#
# @lc app=leetcode.cn id=970 lang=python3
#
# [970] 强整数
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        def powers(base):
            values = [1]
            while base != 1 and values[-1] * base <= bound:
                values.append(values[-1] * base)
            return values

        return list(
            {
                first + second
                for first in powers(x)
                for second in powers(y)
                if first + second <= bound
            }
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.powerfulIntegers, (2, 3, 10), {2, 3, 4, 5, 7, 9, 10}),
        (solution.powerfulIntegers, (3, 5, 15), {2, 4, 6, 8, 10, 14}),
        (solution.powerfulIntegers, (1, 1, 1), set()),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert set(result) == expected
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
