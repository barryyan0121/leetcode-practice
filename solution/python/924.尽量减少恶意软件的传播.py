#
# @lc app=leetcode.cn id=924 lang=python3
#
# [924] 尽量减少恶意软件的传播
#

import os
import sys
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        parent = list(range(n))
        size = [1] * n

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(first, second):
            first, second = find(first), find(second)
            if first == second:
                return
            if size[first] < size[second]:
                first, second = second, first
            parent[second] = first
            size[first] += size[second]

        for first in range(n):
            for second in range(first):
                if graph[first][second]:
                    union(first, second)

        infected = Counter(find(node) for node in initial)
        answer, saved = min(initial), 0
        for node in sorted(initial):
            root = find(node)
            if infected[root] == 1 and size[root] > saved:
                answer, saved = node, size[root]
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minMalwareSpread, ([[1, 1, 0], [1, 1, 0], [0, 0, 1]], [0, 1]), 0),
        (solution.minMalwareSpread, ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [0, 2]), 0),
        (solution.minMalwareSpread, ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 2]), 1),
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
