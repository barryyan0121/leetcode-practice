#
# @lc app=leetcode.cn id=862 lang=python3
#
# [862] 和至少为 K 的最短子数组
#

import os
import sys
from collections import deque
from typing import List


# @lc code=start
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix = 0
        prefixes = [0]
        candidates = deque([0])
        answer = len(nums) + 1
        for index, number in enumerate(nums, 1):
            prefix += number
            prefixes.append(prefix)
            while candidates and prefix - prefixes[candidates[0]] >= k:
                answer = min(answer, index - candidates.popleft())
            while candidates and prefixes[candidates[-1]] >= prefix:
                candidates.pop()
            candidates.append(index)
        return answer if answer <= len(nums) else -1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.shortestSubarray, ([1], 1), 1),
        (solution.shortestSubarray, ([1, 2], 4), -1),
        (solution.shortestSubarray, ([2, -1, 2], 3), 3),
        (solution.shortestSubarray, ([84, -37, 32, 40, 95], 167), 3),
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
