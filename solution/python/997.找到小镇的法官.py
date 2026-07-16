#
# @lc app=leetcode.cn id=997 lang=python3
#
# [997] 找到小镇的法官
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        score = [0] * (n + 1)
        for person, trusted in trust:
            score[person] -= 1
            score[trusted] += 1
        return next(
            (person for person in range(1, n + 1) if score[person] == n - 1), -1
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.findJudge, (2, [[1, 2]]), 2),
        (solution.findJudge, (3, [[1, 3], [2, 3]]), 3),
        (solution.findJudge, (3, [[1, 3], [2, 3], [3, 1]]), -1),
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
