#
# @lc app=leetcode.cn id=963 lang=python3
#
# [963] 最小面积矩形 II
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        point_set = {tuple(point) for point in points}
        answer = float("inf")
        for first in range(len(points)):
            ax, ay = points[first]
            for second in range(len(points)):
                if second == first:
                    continue
                bx, by = points[second]
                for third in range(second):
                    if third == first:
                        continue
                    cx, cy = points[third]
                    if (bx - ax) * (cx - ax) + (by - ay) * (cy - ay):
                        continue
                    if (bx + cx - ax, by + cy - ay) in point_set:
                        area = abs((bx - ax) * (cy - ay) - (by - ay) * (cx - ax))
                        answer = min(answer, area)
        return 0 if answer == float("inf") else answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minAreaFreeRect, ([[1, 2], [2, 1], [1, 0], [0, 1]],), 2.0),
        (solution.minAreaFreeRect, ([[0, 1], [2, 1], [1, 1], [1, 0], [2, 0]],), 1.0),
        (solution.minAreaFreeRect, ([[0, 3], [1, 2], [3, 1], [1, 3], [2, 1]],), 0),
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
