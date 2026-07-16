#
# @lc app=leetcode.cn id=967 lang=python3
#
# [967] 连续差相同的数字
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        numbers = list(range(10)) if n == 1 else list(range(1, 10))
        for _ in range(n - 1):
            updated = []
            for number in numbers:
                last = number % 10
                for digit in {last - k, last + k}:
                    if 0 <= digit <= 9:
                        updated.append(number * 10 + digit)
            numbers = updated
        return numbers


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numsSameConsecDiff, (3, 7), {181, 292, 707, 818, 929}),
        (
            solution.numsSameConsecDiff,
            (2, 1),
            {10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98},
        ),
        (solution.numsSameConsecDiff, (1, 0), set(range(10))),
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
