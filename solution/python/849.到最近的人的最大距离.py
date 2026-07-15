#
# @lc app=leetcode.cn id=849 lang=python3
#
# [849] 到最近的人的最大距离
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        answer = 0
        previous = -1
        for index, occupied in enumerate(seats):
            if occupied:
                answer = index if previous < 0 else max(answer, (index - previous) // 2)
                previous = index
        return max(answer, len(seats) - previous - 1)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.maxDistToClosest, ([1, 0, 0, 0, 1, 0, 1],), 2),
        (solution.maxDistToClosest, ([1, 0, 0, 0],), 3),
        (solution.maxDistToClosest, ([0, 1],), 1),
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
