#
# @lc app=leetcode.cn id=335 lang=python3
# @lcpr version=30203
#
# [335] 路径交叉
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        for i in range(3, len(distance)):
            if distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]:
                return True
            if (
                i >= 4
                and distance[i - 1] == distance[i - 3]
                and distance[i] + distance[i - 4] >= distance[i - 2]
            ):
                return True
            if (
                i >= 5
                and distance[i - 2] >= distance[i - 4]
                and distance[i] + distance[i - 4] >= distance[i - 2]
                and distance[i - 1] <= distance[i - 3]
                and distance[i - 1] + distance[i - 5] >= distance[i - 3]
            ):
                return True
        return False
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.isSelfCrossing, [[2, 1, 1, 2]], True),
        (solution.isSelfCrossing, [[1, 2, 3, 4]], False),
        (solution.isSelfCrossing, [[1, 1, 1, 1]], True),
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
# [2,1,1,2]\n
# @lcpr case=end

#
