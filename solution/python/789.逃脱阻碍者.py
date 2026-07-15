#
# @lc app=leetcode.cn id=789 lang=python3
#
# [789] 逃脱阻碍者
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        distance = abs(target[0]) + abs(target[1])
        return all(
            abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]) > distance
            for ghost in ghosts
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.escapeGhosts, ([[1, 0], [0, 3]], [0, 1]), True),
        (solution.escapeGhosts, ([[1, 0]], [2, 0]), False),
        (solution.escapeGhosts, ([[2, 0]], [1, 0]), False),
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
