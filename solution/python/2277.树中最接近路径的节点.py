#
# @lc app=leetcode.cn id=2277 lang=python3
# @lcpr version=30203
#
# [2277] 树中最接近路径的节点
#

import os
import sys
from collections import deque

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def closestNode(
        self, n: int, edges: List[List[int]], query: List[List[int]]
    ) -> List[int]:
        graph = [[] for _ in range(n)]
        for left, right in edges:
            graph[left].append(right)
            graph[right].append(left)

        def distances(start: int) -> List[int]:
            result = [-1] * n
            result[start] = 0
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if result[neighbor] == -1:
                        result[neighbor] = result[node] + 1
                        queue.append(neighbor)
            return result

        answer = []
        for start, end, node in query:
            parent = [-1] * n
            parent[start] = start
            queue = deque([start])
            while queue:
                current = queue.popleft()
                if current == end:
                    break
                for neighbor in graph[current]:
                    if parent[neighbor] == -1:
                        parent[neighbor] = current
                        queue.append(neighbor)
            path = []
            current = end
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            distance = distances(node)
            answer.append(min(path, key=lambda candidate: distance[candidate]))
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.closestNode,
            (
                7,
                [[0, 1], [0, 2], [0, 3], [1, 4], [2, 5], [2, 6]],
                [[5, 3, 4], [5, 3, 6]],
            ),
            [0, 2],
        ),
        (solution.closestNode, (3, [[0, 1], [1, 2]], [[0, 1, 2]]), [1]),
        (solution.closestNode, (3, [[0, 1], [1, 2]], [[0, 0, 0]]), [0]),
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
    print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
    sys.exit(1)
