#
# @lc app=leetcode.cn id=939 lang=python3
#
# [939] 最小面积矩形
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = {tuple(point) for point in points}
        answer = float("inf")
        for first in range(len(points)):
            x1, y1 = points[first]
            for second in range(first):
                x2, y2 = points[second]
                if (
                    x1 != x2
                    and y1 != y2
                    and (x1, y2) in point_set
                    and (x2, y1) in point_set
                ):
                    answer = min(answer, abs(x1 - x2) * abs(y1 - y2))
        return 0 if answer == float("inf") else answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minAreaRect, ([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]],), 4),
        (solution.minAreaRect, ([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]],), 2),
        (solution.minAreaRect, ([[1, 1], [1, 2], [1, 3]],), 0),
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
