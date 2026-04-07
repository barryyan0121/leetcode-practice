#
# @lc app=leetcode.cn id=478 lang=python3
# @lcpr version=30203
#
# [478] 在圆内随机生成点
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
import random
import math
from common.node import *


# @lc code=start
class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        r = self.radius * math.sqrt(random.random())
        theta = random.random() * 2 * math.pi
        return [
            self.x_center + r * math.cos(theta),
            self.y_center + r * math.sin(theta),
        ]
        # @lc code=end


if __name__ == "__main__":
    random.seed(0)
    solution = Solution(1.0, 0.0, 0.0)
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.randPoint, [], 1.0),
        (solution.randPoint, [], 1.0),
        (solution.randPoint, [], 1.0),
    ]

    all_passed = True
    for idx, (func, args, expected_radius) in enumerate(test_cases):
        try:
            result = func(*args)
            assert len(result) == 2
            assert (result[0] ** 2 + result[1] ** 2) <= expected_radius**2 + 1e-9
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = 圆内点, 实际 = {result}"
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
# 1.0\n0.0\n0.0\n
# @lcpr case=end

#
