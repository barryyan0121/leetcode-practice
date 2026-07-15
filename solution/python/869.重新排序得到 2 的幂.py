#
# @lc app=leetcode.cn id=869 lang=python3
#
# [869] 重新排序得到 2 的幂
#

import os
import sys


# @lc code=start
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = sorted(str(n))
        return any(digits == sorted(str(1 << power)) for power in range(31))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.reorderedPowerOf2, (1,), True),
        (solution.reorderedPowerOf2, (10,), False),
        (solution.reorderedPowerOf2, (46,), True),
        (solution.reorderedPowerOf2, (24,), False),
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
