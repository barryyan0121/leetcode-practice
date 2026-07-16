#
# @lc app=leetcode.cn id=885 lang=python3
#
# [885] 螺旋矩阵 III
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        answer = [[rStart, cStart]]
        row, column = rStart, cStart
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        steps = 1
        while len(answer) < rows * cols:
            for direction in range(4):
                dr, dc = directions[direction]
                for _ in range(steps):
                    row += dr
                    column += dc
                    if 0 <= row < rows and 0 <= column < cols:
                        answer.append([row, column])
                if direction % 2:
                    steps += 1
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.spiralMatrixIII, (1, 4, 0, 0), [[0, 0], [0, 1], [0, 2], [0, 3]]),
        (
            solution.spiralMatrixIII,
            (2, 2, 0, 1),
            [[0, 1], [1, 1], [1, 0], [0, 0]],
        ),
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
