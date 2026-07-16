#
# @lc app=leetcode.cn id=996 lang=python3
#
# [996] 平方数组的数目
#

import os
import sys
from collections import Counter
from math import isqrt
from typing import List


# @lc code=start
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        counts = Counter(nums)
        values = list(counts)
        square = {
            (first, second): isqrt(first + second) ** 2 == first + second
            for first in values
            for second in values
        }

        def search(previous, remaining):
            if remaining == 0:
                return 1
            result = 0
            for value in values:
                if counts[value] and (previous is None or square[previous, value]):
                    counts[value] -= 1
                    result += search(value, remaining - 1)
                    counts[value] += 1
            return result

        return search(None, len(nums))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numSquarefulPerms, ([1, 17, 8],), 2),
        (solution.numSquarefulPerms, ([2, 2, 2],), 1),
        (solution.numSquarefulPerms, ([1],), 1),
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
