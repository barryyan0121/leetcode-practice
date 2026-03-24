#
# @lc app=leetcode.cn id=85 lang=python3
# @lcpr version=30202
#
# [85] 最大矩形
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        def largest_rectangle_area(heights: List[int]) -> int:
            stack = []
            best = 0
            for i in range(len(heights) + 1):
                cur = heights[i] if i < len(heights) else 0
                while stack and heights[stack[-1]] > cur:
                    h = heights[stack.pop()]
                    left = stack[-1] if stack else -1
                    best = max(best, h * (i - left - 1))
                stack.append(i)
            return best

        heights = [0] * len(matrix[0])
        ans = 0
        for row in matrix:
            for i, ch in enumerate(row):
                heights[i] = heights[i] + 1 if ch == "1" else 0
            ans = max(ans, largest_rectangle_area(heights))
        return ans
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.maximalRectangle,
            [
                [
                    ["1", "0", "1", "0", "0"],
                    ["1", "0", "1", "1", "1"],
                    ["1", "1", "1", "1", "1"],
                    ["1", "0", "0", "1", "0"],
                ]
            ],
            6,
        ),
        (solution.maximalRectangle, [[[]]], 0),
        (solution.maximalRectangle, [[["0"]]], 0),
        (solution.maximalRectangle, [[["1"]]], 1),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)


#
# @lcpr case=start
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["0"]]\n
# @lcpr case=end

#
