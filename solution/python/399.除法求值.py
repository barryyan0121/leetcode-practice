#
# @lc app=leetcode.cn id=399 lang=python3
# @lcpr version=30203
#
# [399] 除法求值
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from collections import defaultdict, deque
from common.node import *


# @lc code=start
class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
    ) -> List[float]:
        graph = defaultdict(list)
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def bfs(start: str, end: str) -> float:
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0

            queue = deque([(start, 1.0)])
            visited = {start}
            while queue:
                node, product = queue.popleft()
                for nxt, weight in graph[node]:
                    if nxt in visited:
                        continue
                    new_product = product * weight
                    if nxt == end:
                        return new_product
                    visited.add(nxt)
                    queue.append((nxt, new_product))
            return -1.0

        return [bfs(a, b) for a, b in queries]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.calcEquation,
            (
                [["a", "b"], ["b", "c"]],
                [2.0, 3.0],
                [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
            ),
            [6.0, 0.5, -1.0, 1.0, -1.0],
        ),
        (
            solution.calcEquation,
            (
                [["a", "b"], ["b", "c"], ["bc", "cd"]],
                [1.5, 2.5, 5.0],
                [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
            ),
            [3.75, 0.4, 5.0, 0.2],
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert all(abs(a - b) < 1e-9 for a, b in zip(result, expected))
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
# [["a","b"],["b","c"]]\n[2.0,3.0]\n[["a","c"]]\n
# @lcpr case=end
