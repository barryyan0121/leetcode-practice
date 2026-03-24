#
# @lc app=leetcode.cn id=149 lang=python3
# @lcpr version=30203
#
# [149] 直线上最多的点数
#

import sys
import os
from collections import defaultdict
from math import gcd

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        ans = 0
        for i in range(n):
            slopes = defaultdict(int)
            same = 1
            cur_best = 0
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                if dx == 0 and dy == 0:
                    same += 1
                    continue
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                if dx < 0:
                    dx = -dx
                    dy = -dy
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1
                slopes[(dx, dy)] += 1
                cur_best = max(cur_best, slopes[(dx, dy)])
            ans = max(ans, cur_best + same)
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.maxPoints, [[[1, 1], [2, 2], [3, 3]]], 3),
        (solution.maxPoints, [[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]], 4),
        (solution.maxPoints, [[[0, 0]]], 1),
        (solution.maxPoints, [[[0, 0], [0, 0]]], 2),
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
# [[1,1],[2,2],[3,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]\n
# @lcpr case=end

#
