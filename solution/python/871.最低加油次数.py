#
# @lc app=leetcode.cn id=871 lang=python3
#
# [871] 最低加油次数
#

import os
import sys
from heapq import heappop, heappush
from typing import List


# @lc code=start
class Solution:
    def minRefuelStops(
        self, target: int, startFuel: int, stations: List[List[int]]
    ) -> int:
        available = []
        fuel = startFuel
        stops = 0
        for position, station_fuel in stations + [[target, 0]]:
            while fuel < position and available:
                fuel -= heappop(available)
                stops += 1
            if fuel < position:
                return -1
            heappush(available, -station_fuel)
        return stops


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minRefuelStops, (1, 1, []), 0),
        (solution.minRefuelStops, (100, 1, [[10, 100]]), -1),
        (
            solution.minRefuelStops,
            (100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]),
            2,
        ),
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
