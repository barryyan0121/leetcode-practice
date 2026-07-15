#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#

import os
import sys
from typing import *


# @lc code=start
class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        original = image[sr][sc]
        if original == color:
            return image
        rows, columns = len(image), len(image[0])
        stack = [(sr, sc)]
        image[sr][sc] = color
        while stack:
            row, column = stack.pop()
            for next_row, next_column in (
                (row - 1, column),
                (row + 1, column),
                (row, column - 1),
                (row, column + 1),
            ):
                if (
                    0 <= next_row < rows
                    and 0 <= next_column < columns
                    and image[next_row][next_column] == original
                ):
                    image[next_row][next_column] = color
                    stack.append((next_row, next_column))
        return image


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.floodFill,
            ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2),
            [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
        ),
        (solution.floodFill, ([[0, 0, 0], [0, 0, 0]], 0, 0, 0), [[0, 0, 0], [0, 0, 0]]),
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
