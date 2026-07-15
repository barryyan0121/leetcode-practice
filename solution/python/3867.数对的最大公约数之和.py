#
# @lc app=leetcode.cn id=3867 lang=python3
#
# [3867] 数对的最大公约数之和
#

import os
import sys
from math import gcd


# @lc code=start
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix_gcd = []
        maximum = 0
        for num in nums:
            maximum = max(maximum, num)
            prefix_gcd.append(gcd(num, maximum))

        velqoradin = sorted(prefix_gcd)
        return sum(
            gcd(velqoradin[i], velqoradin[~i]) for i in range(len(velqoradin) // 2)
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.gcdSum, ([2, 6, 4],), 2),
        (solution.gcdSum, ([3, 6, 2, 8],), 5),
        (solution.gcdSum, ([7],), 0),
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
