#
# @lc app=leetcode.cn id=802 lang=python3
#
# [802] 找到最终的安全状态
#

import os
import sys
from collections import deque
from typing import List


# @lc code=start
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        reverse = [[] for _ in graph]
        outdegree = list(map(len, graph))
        for node, neighbors in enumerate(graph):
            for neighbor in neighbors:
                reverse[neighbor].append(node)

        queue = deque(node for node, degree in enumerate(outdegree) if degree == 0)
        safe = [False] * len(graph)
        while queue:
            node = queue.popleft()
            safe[node] = True
            for previous in reverse[node]:
                outdegree[previous] -= 1
                if outdegree[previous] == 0:
                    queue.append(previous)
        return [node for node, is_safe in enumerate(safe) if is_safe]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.eventualSafeNodes,
            ([[1, 2], [2, 3], [5], [0], [5], [], []],),
            [2, 4, 5, 6],
        ),
        (
            solution.eventualSafeNodes,
            ([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []],),
            [4],
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
