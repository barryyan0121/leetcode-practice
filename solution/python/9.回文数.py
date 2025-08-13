#
# @lc app=leetcode.cn id=9 lang=python3
# @lcpr version=30202
#
# [9] 回文数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        y = 0
        while temp > 0:
            y = y * 10 + temp % 10
            temp //= 10
        return x == y


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    # your test code here
    # 测试用例
    test_cases = [(121, True), (-121, False), (10, False), (12321, True), (12345, False), (123456, False)]

    all_passed = True
    for idx, (n, expected) in enumerate(test_cases):
        try:
            result = solution.isPalindrome(n)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n={n}, result={result}")
        except AssertionError:
            all_passed = False
            print(f"测试用例 {idx + 1} 失败: n={n}, 期望={expected}, 实际={result}")

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
# 121\n
# @lcpr case=end

# @lcpr case=start
# -121\n
# @lcpr case=end

# @lcpr case=start
# 10\n
# @lcpr case=end

#
