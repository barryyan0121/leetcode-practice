#
# @lc app=leetcode.cn id=517 lang=python3
# @lcpr version=30203
#
# [517] 超级洗衣机
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        n = len(machines)
        if total % n != 0:
            return -1

        avg = total // n
        ans = 0
        balance = 0
        for load in machines:
            diff = load - avg
            balance += diff
            ans = max(ans, abs(balance), diff)
        return ans


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (solution.findMinMoves, ([1, 0, 5],), 3),
        (solution.findMinMoves, ([0, 3, 0],), 2),
        (solution.findMinMoves, ([0, 2, 0],), -1),
        (solution.findMinMoves, ([4, 0, 0, 4],), 2),
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
# [1,0,5]\n
# @lcpr case=end
#
