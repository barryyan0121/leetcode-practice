#
# @lc app=leetcode.cn id=850 lang=python3
#
# [850] 矩形面积 II
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        events = []
        for index, (left, bottom, right, top) in enumerate(rectangles):
            events.append((left, 1, index, bottom, top))
            events.append((right, -1, index, bottom, top))
        events.sort()

        active = {}
        area = 0
        previous_x = events[0][0]
        for x, change, index, bottom, top in events:
            covered = 0
            end = -1
            for start, stop in sorted(active.values()):
                if start > end:
                    covered += stop - start
                    end = stop
                elif stop > end:
                    covered += stop - end
                    end = stop
            area += (x - previous_x) * covered
            if change == 1:
                active[index] = bottom, top
            else:
                del active[index]
            previous_x = x
        return area % (10**9 + 7)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.rectangleArea,
            ([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]],),
            6,
        ),
        (solution.rectangleArea, ([[0, 0, 1000000000, 1000000000]],), 49),
        (solution.rectangleArea, ([[0, 0, 1, 1], [1, 0, 2, 1]],), 2),
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
