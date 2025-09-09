#
# @lc app=leetcode.cn id=3516 lang=python3
# @lcpr version=30202
#
# [3516] 找到最近的人
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a = abs(x - z)
        b = abs(y - z)
        if a < b:
            return 1
        elif a > b:
            return 2
        else:
            return 0

        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.findClosest, (2, 7, 4), 1),
        (solution.findClosest, (2, 5, 6), 2),
        (solution.findClosest, (1, 5, 3), 0),
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
# 2\n7\n4\n
# @lcpr case=end

# @lcpr case=start
# 2\n5\n6\n
# @lcpr case=end

# @lcpr case=start
# 1\n5\n3\n
# @lcpr case=end

#
