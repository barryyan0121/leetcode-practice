#
# @lc app=leetcode.cn id=753 lang=python3
#
# [753] 破解保险箱
#

import os
import sys


# @lc code=start
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        start = "0" * (n - 1)
        visited = set()
        answer = []

        def dfs(node: str) -> None:
            for digit in map(str, range(k)):
                edge = node + digit
                if edge not in visited:
                    visited.add(edge)
                    dfs(edge[1:])
                    answer.append(digit)

        dfs(start)
        return "".join(answer) + start


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.crackSafe, (1, 2), {"0", "1"}),
        (solution.crackSafe, (2, 2), {"00", "01", "10", "11"}),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        n, k = args
        try:
            assert len(result) == k**n + n - 1
            assert {result[i : i + n] for i in range(len(result) - n + 1)} == expected
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
