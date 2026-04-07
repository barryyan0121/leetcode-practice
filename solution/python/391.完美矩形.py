#
# @lc app=leetcode.cn id=391 lang=python3
# @lcpr version=30203
#
# [391] 完美矩形
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        min_x = min_y = float("inf")
        max_x = max_y = float("-inf")
        corners = set()

        for x1, y1, x2, y2 in rectangles:
            area += (x2 - x1) * (y2 - y1)
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)

            for corner in ((x1, y1), (x1, y2), (x2, y1), (x2, y2)):
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)

        return (
            area == (max_x - min_x) * (max_y - min_y)
            and corners
            == {
                (min_x, min_y),
                (min_x, max_y),
                (max_x, min_y),
                (max_x, max_y),
            }
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.isRectangleCover,
            ([[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]],),
            True,
        ),
        (
            solution.isRectangleCover,
            ([[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]],),
            False,
        ),
        (
            solution.isRectangleCover,
            ([[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [3, 2, 4, 4]],),
            False,
        ),
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
# [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]\n
# @lcpr case=end
