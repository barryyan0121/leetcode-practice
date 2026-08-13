#
# @lc app=leetcode.cn id=3896 lang=python3
#
# [3896] 将数组变成交替质数的最少操作次数
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def is_prime(value: int) -> bool:
            if value < 2:
                return False
            if value % 2 == 0:
                return value == 2
            factor = 3
            while factor * factor <= value:
                if value % factor == 0:
                    return False
                factor += 2
            return True

        answer = 0
        for index, num in enumerate(nums):
            target = num
            if index % 2 == 0:
                while not is_prime(target):
                    target += 1
            else:
                while is_prime(target):
                    target += 1
            answer += target - num
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.minOperations, ([1, 2, 3, 4],), 3),
        (solution.minOperations, ([5, 6, 7, 8],), 0),
        (solution.minOperations, ([4, 4],), 1),
        (solution.minOperations, ([2, 3, 5],), 1),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: args = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: args = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
