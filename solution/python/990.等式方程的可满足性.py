#
# @lc app=leetcode.cn id=990 lang=python3
#
# [990] 等式方程的可满足性
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = list(range(26))

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for equation in equations:
            if equation[1] == "=":
                first, second = map(
                    lambda letter: ord(letter) - ord("a"), equation[::3]
                )
                parent[find(first)] = find(second)
        return all(
            equation[1] == "="
            or find(ord(equation[0]) - ord("a")) != find(ord(equation[3]) - ord("a"))
            for equation in equations
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.equationsPossible, (["a==b", "b!=a"],), False),
        (solution.equationsPossible, (["b==a", "a==b"],), True),
        (solution.equationsPossible, (["a==b", "b==c", "a==c"],), True),
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
