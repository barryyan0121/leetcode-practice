#
# @lc app=leetcode.cn id=277 lang=python3
# @lcpr version=30203
#
# [277] 搜寻名人
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


def knows(a: int, b: int) -> bool:  # pragma: no cover
    raise NotImplementedError


# @lc code=start
class Solution:
    def findCelebrity(self, n: int) -> int:
        cand = 0
        for i in range(1, n):
            if knows(cand, i):
                cand = i

        for i in range(n):
            if i == cand:
                continue
            if knows(cand, i) or not knows(i, cand):
                return -1
        return cand


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def run_case(matrix: List[List[bool]], n: int) -> int:
        def mock_knows(a: int, b: int) -> bool:
            return matrix[a][b]

        globals()["knows"] = mock_knows
        return solution.findCelebrity(n)

    # 测试用例 (func, args, result)
    test_cases = [
        (
            run_case,
            (
                [
                    [False, True, True],
                    [False, False, True],
                    [False, False, False],
                ],
                3,
            ),
            2,
        ),
        (
            run_case,
            (
                [
                    [False, True, False],
                    [False, False, False],
                    [True, True, False],
                ],
                3,
            ),
            1,
        ),
        (
            run_case,
            (
                [
                    [False, True],
                    [True, False],
                ],
                2,
            ),
            -1,
        ),
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
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)


#
# @lcpr case=start
# n = 3\n
# @lcpr case=end
