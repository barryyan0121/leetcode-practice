#
# @lc app=leetcode.cn id=797 lang=python3
#
# [797] 所有可能的路径
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        answer = []

        def search(node: int, path: List[int]) -> None:
            if node == target:
                answer.append(path)
                return
            for neighbor in graph[node]:
                search(neighbor, path + [neighbor])

        search(0, [0])
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.allPathsSourceTarget,
            ([[1, 2], [3], [3], []],),
            [[0, 1, 3], [0, 2, 3]],
        ),
        (
            solution.allPathsSourceTarget,
            ([[4, 3, 1], [3, 2, 4], [3], [4], []],),
            [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]],
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
