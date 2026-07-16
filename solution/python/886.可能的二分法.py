#
# @lc app=leetcode.cn id=886 lang=python3
#
# [886] 可能的二分法
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for first, second in dislikes:
            graph[first - 1].append(second - 1)
            graph[second - 1].append(first - 1)

        colors = [0] * n
        for start in range(n):
            if colors[start]:
                continue
            colors[start] = 1
            stack = [start]
            while stack:
                person = stack.pop()
                for neighbor in graph[person]:
                    if colors[neighbor] == colors[person]:
                        return False
                    if not colors[neighbor]:
                        colors[neighbor] = -colors[person]
                        stack.append(neighbor)
        return True


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.possibleBipartition, (4, [[1, 2], [1, 3], [2, 4]]), True),
        (solution.possibleBipartition, (3, [[1, 2], [1, 3], [2, 3]]), False),
        (
            solution.possibleBipartition,
            (5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]),
            False,
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
