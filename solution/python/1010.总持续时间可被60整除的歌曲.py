#
# @lc app=leetcode.cn id=1010 lang=python3
#
# [1010] 总持续时间可被 60 整除的歌曲
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counts = [0] * 60
        pairs = 0
        for duration in time:
            remainder = duration % 60
            pairs += counts[-remainder % 60]
            counts[remainder] += 1
        return pairs


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.numPairsDivisibleBy60, ([30, 20, 150, 100, 40],), 3),
        (solution.numPairsDivisibleBy60, ([60, 60, 60],), 3),
        (solution.numPairsDivisibleBy60, ([10, 50],), 1),
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
