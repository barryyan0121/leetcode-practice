#
# @lc app=leetcode.cn id=974 lang=python3
#
# [974] 和可被 K 整除的子数组
#

import os
import sys
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainders = Counter({0: 1})
        remainder = answer = 0
        for number in nums:
            remainder = (remainder + number) % k
            answer += remainders[remainder]
            remainders[remainder] += 1
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.subarraysDivByK, ([4, 5, 0, -2, -3, 1], 5), 7),
        (solution.subarraysDivByK, ([5], 9), 0),
        (solution.subarraysDivByK, ([0, 0], 1), 3),
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
