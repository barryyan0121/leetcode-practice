#
# @lc app=leetcode.cn id=1040 lang=python3
#
# [1040] 移动石子直到连续 II
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        length = len(stones)
        maximum = max(
            stones[-1] - stones[1] - length + 2,
            stones[-2] - stones[0] - length + 2,
        )
        minimum = length
        left = 0
        for right, stone in enumerate(stones):
            while stone - stones[left] + 1 > length:
                left += 1
            count = right - left + 1
            if count == length - 1 and stone - stones[left] == length - 2:
                minimum = min(minimum, 2)
            else:
                minimum = min(minimum, length - count)
        return [minimum, maximum]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numMovesStonesII, ([7, 4, 9],), [1, 2]),
        (solution.numMovesStonesII, ([6, 5, 4, 3, 10],), [2, 3]),
        (solution.numMovesStonesII, ([100, 101, 104, 102, 103],), [0, 0]),
        (solution.numMovesStonesII, ([1, 2, 3, 4, 10],), [2, 5]),
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
