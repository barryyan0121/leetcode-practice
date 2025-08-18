#
# @lc app=leetcode.cn id=1323 lang=python3
# @lcpr version=30202
#
# [1323] 6 和 9 组成的最大数字
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def maximum69Number(self, num: int) -> int:
        # 将数字转换为字符串，找到第一个6并替换为9
        num_str = str(num)
        if "6" in num_str:
            num_str = num_str.replace("6", "9", 1)
        return int(num_str)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.maximum69Number, (9669,), 9969),
        (solution.maximum69Number, (9996,), 9999),
        (solution.maximum69Number, (9999,), 9999),
        (solution.maximum69Number, (6666,), 9666),
        (solution.maximum69Number, (6969,), 9969),
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
# 9669\n
# @lcpr case=end

# @lcpr case=start
# 9996\n
# @lcpr case=end

# @lcpr case=start
# 9999\n
# @lcpr case=end

#
