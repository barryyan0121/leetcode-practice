#
# @lc app=leetcode.cn id=928 lang=python3
#
# [928] 尽量减少恶意软件的传播 II
#

import os
import sys
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        infected = set(initial)
        visited = set()
        saved = Counter()
        for start in range(len(graph)):
            if start in infected or start in visited:
                continue
            component = []
            sources = set()
            stack = [start]
            visited.add(start)
            while stack:
                node = stack.pop()
                component.append(node)
                for neighbor, connected in enumerate(graph[node]):
                    if not connected:
                        continue
                    if neighbor in infected:
                        sources.add(neighbor)
                    elif neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
            if len(sources) == 1:
                saved[sources.pop()] += len(component)
        return min(initial, key=lambda node: (-saved[node], node))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minMalwareSpread, ([[1, 1, 0], [1, 1, 0], [0, 0, 1]], [0, 1]), 0),
        (solution.minMalwareSpread, ([[1, 1, 0], [1, 1, 1], [0, 1, 1]], [0, 1]), 1),
        (
            solution.minMalwareSpread,
            ([[1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 1, 1], [0, 0, 1, 1]], [0, 3]),
            0,
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
