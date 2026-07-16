#
# @lc app=leetcode.cn id=1029 lang=python3
#
# [1029] 两地调度
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda cost: cost[0] - cost[1])
        half = len(costs) // 2
        return sum(cost[0] for cost in costs[:half]) + sum(
            cost[1] for cost in costs[half:]
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.twoCitySchedCost, ([[10, 20], [30, 200], [400, 50], [30, 20]],), 110),
        (
            solution.twoCitySchedCost,
            ([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]],),
            1859,
        ),
        (solution.twoCitySchedCost, ([[1, 2], [2, 1]],), 2),
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
