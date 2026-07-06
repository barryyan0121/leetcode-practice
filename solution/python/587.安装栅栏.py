#
# @lc app=leetcode.cn id=587 lang=python3
# @lcpr version=30203
#
# [587] 安装栅栏
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        points = sorted(map(tuple, trees))
        if len(points) <= 1:
            return [list(point) for point in points]

        def cross(o: Tuple[int, int], a: Tuple[int, int], b: Tuple[int, int]) -> int:
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        lower = []
        for point in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], point) < 0:
                lower.pop()
            lower.append(point)

        upper = []
        for point in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], point) < 0:
                upper.pop()
            upper.append(point)

        return [list(point) for point in set(lower + upper)]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def normalize(points: List[List[int]]) -> List[List[int]]:
        return sorted(points)

    test_cases = [
        (
            solution.outerTrees,
            ([[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]],),
            [[1, 1], [2, 0], [2, 4], [3, 3], [4, 2]],
        ),
        (solution.outerTrees, ([[1, 2], [2, 2], [4, 2]],), [[1, 2], [2, 2], [4, 2]]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert normalize(result) == normalize(expected)
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
# [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[2,2],[4,2]]\n
# @lcpr case=end

#
