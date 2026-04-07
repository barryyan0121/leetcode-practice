#
# @lc app=leetcode.cn id=393 lang=python3
# @lcpr version=30203
#
# [393] UTF-8 编码验证
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        remaining = 0
        for num in data:
            if remaining == 0:
                if num >> 7 == 0:
                    continue
                mask = 0b10000000
                while num & mask:
                    remaining += 1
                    mask >>= 1
                if remaining == 1 or remaining > 4:
                    return False
                remaining -= 1
            else:
                if num >> 6 != 0b10:
                    return False
                remaining -= 1
        return remaining == 0


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.validUtf8, ([197, 130, 1],), True),
        (solution.validUtf8, ([235, 140, 4],), False),
        (solution.validUtf8, ([0],), True),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)


#
# @lcpr case=start
# [197,130,1]\n
# @lcpr case=end
