#
# @lc app=leetcode.cn id=798 lang=python3
#
# [798] 得分最高的最小轮调
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        size = len(nums)
        changes = [0] * size
        score = sum(number <= index for index, number in enumerate(nums))
        for index, number in enumerate(nums):
            if number:
                changes[(index - number + 1) % size] -= 1
                changes[(index + 1) % size] += 1

        answer = 0
        best = score
        for rotation in range(1, size):
            score += changes[rotation]
            if score > best:
                best = score
                answer = rotation
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.bestRotation, ([2, 3, 1, 4, 0],), 3),
        (solution.bestRotation, ([1, 3, 0, 2, 4],), 0),
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
