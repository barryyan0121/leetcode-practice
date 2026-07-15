#
# @lc app=leetcode.cn id=826 lang=python3
#
# [826] 安排工作以达到最大收益
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        jobs = sorted(zip(difficulty, profit))
        answer = best = index = 0
        for ability in sorted(worker):
            while index < len(jobs) and jobs[index][0] <= ability:
                best = max(best, jobs[index][1])
                index += 1
            answer += best
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.maxProfitAssignment,
            ([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7]),
            100,
        ),
        (solution.maxProfitAssignment, ([85, 47, 57], [24, 66, 99], [40, 25, 25]), 0),
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
