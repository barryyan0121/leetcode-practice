#
# @lc app=leetcode.cn id=834 lang=python3
#
# [834] 树中距离之和
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        parent = [-1] * n
        parent[0] = 0
        order = [0]
        for node in order:
            for neighbor in graph[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    order.append(neighbor)

        subtree = [1] * n
        answer = [0] * n
        for node in reversed(order[1:]):
            subtree[parent[node]] += subtree[node]
            answer[0] += subtree[node]
        for node in order[1:]:
            answer[node] = answer[parent[node]] + n - 2 * subtree[node]
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.sumOfDistancesInTree,
            (6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]),
            [8, 12, 6, 10, 10, 10],
        ),
        (solution.sumOfDistancesInTree, (1, []), [0]),
        (solution.sumOfDistancesInTree, (2, [[1, 0]]), [1, 1]),
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
