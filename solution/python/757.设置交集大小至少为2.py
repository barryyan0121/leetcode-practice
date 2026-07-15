#
# @lc app=leetcode.cn id=757 lang=python3
#
# [757] 设置交集大小至少为 2
#

import os
import sys
from typing import *


# @lc code=start
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        first = second = -1
        answer = 0
        for left, right in sorted(
            intervals, key=lambda interval: (interval[1], -interval[0])
        ):
            if left > second:
                answer += 2
                first, second = right - 1, right
            elif left > first:
                answer += 1
                first, second = second, right
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.intersectionSizeTwo, ([[1, 3], [3, 7], [8, 9]],), 5),
        (solution.intersectionSizeTwo, ([[1, 3], [1, 4], [2, 5], [3, 5]],), 3),
        (solution.intersectionSizeTwo, ([[1, 2], [2, 3], [2, 4], [4, 5]],), 5),
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
