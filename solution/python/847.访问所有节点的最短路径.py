#
# @lc app=leetcode.cn id=847 lang=python3
#
# [847] 访问所有节点的最短路径
#

import os
import sys
from collections import deque
from typing import List


# @lc code=start
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        target = (1 << len(graph)) - 1
        queue = deque((node, 1 << node, 0) for node in range(len(graph)))
        visited = {(node, 1 << node) for node in range(len(graph))}
        while queue:
            node, mask, distance = queue.popleft()
            if mask == target:
                return distance
            for neighbor in graph[node]:
                state = neighbor, mask | 1 << neighbor
                if state not in visited:
                    visited.add(state)
                    queue.append((*state, distance + 1))
        return 0


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.shortestPathLength, ([[1, 2, 3], [0], [0], [0]],), 4),
        (
            solution.shortestPathLength,
            ([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]],),
            4,
        ),
        (solution.shortestPathLength, ([[]],), 0),
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
