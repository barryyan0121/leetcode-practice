#
# @lc app=leetcode.cn id=178 lang=python3
# @lcpr version=30203
#
# [178] 分数排名
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def rankScores(self, scores: List[int]) -> List[List[int]]:
        ranked = []
        rank = 1
        for score in sorted(set(scores), reverse=True):
            ranked.append([score, rank])
            rank += 1
        return ranked


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.rankScores, ([3, 3, 2, 1],), [[3, 1], [2, 2], [1, 3]]),
        (solution.rankScores, ([10],), [[10, 1]]),
        (solution.rankScores, ([1, 2, 2, 3],), [[3, 1], [2, 2], [1, 3]]),
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
# [3,3,2,1]\n
# @lcpr case=end
