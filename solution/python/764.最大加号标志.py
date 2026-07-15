#
# @lc app=leetcode.cn id=764 lang=python3
#
# [764] 最大加号标志
#

import os
import sys
from typing import *


# @lc code=start
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        blocked = {tuple(mine) for mine in mines}
        lengths = [[0] * n for _ in range(n)]
        for row in range(n):
            count = 0
            for column in range(n):
                count = 0 if (row, column) in blocked else count + 1
                lengths[row][column] = count
            count = 0
            for column in range(n - 1, -1, -1):
                count = 0 if (row, column) in blocked else count + 1
                lengths[row][column] = min(lengths[row][column], count)
        answer = 0
        for column in range(n):
            count = 0
            for row in range(n):
                count = 0 if (row, column) in blocked else count + 1
                lengths[row][column] = min(lengths[row][column], count)
            count = 0
            for row in range(n - 1, -1, -1):
                count = 0 if (row, column) in blocked else count + 1
                answer = max(answer, min(lengths[row][column], count))
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.orderOfLargestPlusSign, (5, [[4, 2]]), 2),
        (solution.orderOfLargestPlusSign, (1, [[0, 0]]), 0),
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
