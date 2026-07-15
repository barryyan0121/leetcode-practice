#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#

import os
import sys
from typing import *


# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first, count = {}, {}
        degree = answer = 0
        for i, number in enumerate(nums):
            first.setdefault(number, i)
            count[number] = count.get(number, 0) + 1
            length = i - first[number] + 1
            if count[number] > degree:
                degree, answer = count[number], length
            elif count[number] == degree:
                answer = min(answer, length)
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.findShortestSubArray, ([1, 2, 2, 3, 1],), 2),
        (solution.findShortestSubArray, ([1, 2, 2, 3, 1, 4, 2],), 6),
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
