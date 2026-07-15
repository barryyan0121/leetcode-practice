#
# @lc app=leetcode.cn id=815 lang=python3
#
# [815] 公交路线
#

import os
import sys
from collections import defaultdict, deque
from typing import List


# @lc code=start
class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0
        stop_to_routes = defaultdict(list)
        for route, stops in enumerate(routes):
            for stop in stops:
                stop_to_routes[stop].append(route)

        queue = deque([source])
        seen_stops = {source}
        seen_routes = set()
        buses = 0
        while queue:
            buses += 1
            for _ in range(len(queue)):
                stop = queue.popleft()
                for route in stop_to_routes[stop]:
                    if route in seen_routes:
                        continue
                    seen_routes.add(route)
                    for next_stop in routes[route]:
                        if next_stop == target:
                            return buses
                        if next_stop not in seen_stops:
                            seen_stops.add(next_stop)
                            queue.append(next_stop)
        return -1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numBusesToDestination, ([[1, 2, 7], [3, 6, 7]], 1, 6), 2),
        (
            solution.numBusesToDestination,
            ([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12),
            -1,
        ),
        (solution.numBusesToDestination, ([[1, 2, 3]], 2, 2), 0),
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
