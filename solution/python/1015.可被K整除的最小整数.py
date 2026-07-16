#
# @lc app=leetcode.cn id=1015 lang=python3
#
# [1015] 可被 K 整除的最小整数
#

import os
import sys


# @lc code=start
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        remainder = 0
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length
        return -1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.smallestRepunitDivByK, (1,), 1),
        (solution.smallestRepunitDivByK, (2,), -1),
        (solution.smallestRepunitDivByK, (3,), 3),
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
