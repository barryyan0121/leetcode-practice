#
# @lc app=leetcode.cn id=469 lang=python3
# @lcpr version=30203
#
# [469] 凸多边形
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        if len(points) < 3:
            return False

        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        sign = 0
        n = len(points)
        for i in range(n):
            c = cross(points[i], points[(i + 1) % n], points[(i + 2) % n])
            if c == 0:
                return False
            if sign == 0:
                sign = 1 if c > 0 else -1
            elif sign * c < 0:
                return False
        return True
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.isConvex, [[[0, 0], [0, 1], [1, 1], [1, 0]]], True),
        (solution.isConvex, [[[0, 0], [0, 10], [10, 10], [10, 0], [5, 5]]], False),
        (solution.isConvex, [[[0, 0], [1, 1], [2, 0]]], True),
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
# [[0,0],[0,1],[1,1],[1,0]]\n
# @lcpr case=end

#
