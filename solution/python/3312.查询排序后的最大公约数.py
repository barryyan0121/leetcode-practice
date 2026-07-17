#
# @lc app=leetcode.cn id=3312 lang=python3
#
# [3312] 查询排序后的最大公约数
#

import os
import sys
from bisect import bisect_right


# @lc code=start
class Solution:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
        maximum = max(nums)
        frequency = [0] * (maximum + 1)
        for num in nums:
            frequency[num] += 1

        pairs = [0] * (maximum + 1)
        for gcd in range(maximum, 0, -1):
            count = sum(frequency[gcd::gcd])
            pairs[gcd] = count * (count - 1) // 2 - sum(pairs[gcd * 2 :: gcd])

        for gcd in range(1, maximum + 1):
            pairs[gcd] += pairs[gcd - 1]
        return [bisect_right(pairs, query) for query in queries]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.gcdValues, ([2, 3, 4], [0, 2, 2]), [1, 2, 2]),
        (solution.gcdValues, ([4, 4, 2, 1], [5, 3, 1, 0]), [4, 2, 1, 1]),
        (solution.gcdValues, ([2, 2], [0, 0]), [2, 2]),
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
