#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [0] * len(graph)
        for start in range(len(graph)):
            if colors[start]:
                continue
            colors[start] = 1
            stack = [start]
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if colors[neighbor] == colors[node]:
                        return False
                    if not colors[neighbor]:
                        colors[neighbor] = -colors[node]
                        stack.append(neighbor)
        return True


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.isBipartite, ([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]],), False),
        (solution.isBipartite, ([[1, 3], [0, 2], [1, 3], [0, 2]],), True),
        (solution.isBipartite, ([[]],), True),
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
