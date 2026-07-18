#
# @lc app=leetcode.cn id=1033 lang=python3
#
# [1033] 移动石子直到连续
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted((a, b, c))
        maximum = c - a - 2
        if b - a == c - b == 1:
            minimum = 0
        elif b - a <= 2 or c - b <= 2:
            minimum = 1
        else:
            minimum = 2
        return [minimum, maximum]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numMovesStones, (1, 2, 5), [1, 2]),
        (solution.numMovesStones, (4, 3, 2), [0, 0]),
        (solution.numMovesStones, (3, 5, 1), [1, 2]),
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
