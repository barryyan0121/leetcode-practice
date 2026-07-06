#
# @lc app=leetcode.cn id=593 lang=python3
# @lcpr version=30203
#
# [593] 有效的正方形
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def validSquare(
        self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]
    ) -> bool:
        points = [p1, p2, p3, p4]
        distances = []
        for i in range(4):
            for j in range(i + 1, 4):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                distances.append(dx * dx + dy * dy)

        distances.sort()
        return (
            distances[0] > 0
            and distances[0] == distances[1] == distances[2] == distances[3]
            and distances[4] == distances[5] == 2 * distances[0]
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.validSquare, ([0, 0], [1, 1], [1, 0], [0, 1]), True),
        (solution.validSquare, ([0, 0], [1, 1], [1, 0], [0, 12]), False),
        (solution.validSquare, ([1, 0], [-1, 0], [0, 1], [0, -1]), True),
        (solution.validSquare, ([0, 0], [0, 0], [0, 0], [0, 0]), False),
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
# [0,0]\n[1,1]\n[1,0]\n[0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0]\n[1,1]\n[1,0]\n[0,12]\n
# @lcpr case=end

#
