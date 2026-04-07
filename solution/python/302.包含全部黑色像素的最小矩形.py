#
# @lc app=leetcode.cn id=302 lang=python3
# @lcpr version=30203
#
# [302] 包含全部黑色像素的最小矩形
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        rows, cols = len(image), len(image[0])
        top = bottom = x
        left = right = y

        for r in range(rows):
            for c in range(cols):
                if image[r][c] == "1":
                    top = min(top, r)
                    bottom = max(bottom, r)
                    left = min(left, c)
                    right = max(right, c)

        return (bottom - top + 1) * (right - left + 1)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.minArea, ([["0", "0", "1", "0"], ["0", "1", "1", "0"], ["0", "1", "0", "0"]], 0, 2), 6),
        (solution.minArea, ([["1"]], 0, 0), 1),
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
# [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]]\n0\n2\n
# @lcpr case=end
