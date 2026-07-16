#
# @lc app=leetcode.cn id=1009 lang=python3
#
# [1009] 十进制整数的反码
#

import os
import sys


# @lc code=start
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        mask = (1 << max(1, n.bit_length())) - 1
        return n ^ mask


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.bitwiseComplement, (5,), 2),
        (solution.bitwiseComplement, (7,), 0),
        (solution.bitwiseComplement, (0,), 1),
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
