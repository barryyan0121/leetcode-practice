#
# @lc app=leetcode.cn id=326 lang=python3
# @lcpr version=30202
#
# [326] 3 的幂
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3**19 % n == 0
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # your test code here
    # 测试用例
    test_cases = [
        (27, True),
        (0, False),
        (9, True),
        (45, False),
        (1, True),
        (3**19, True),
        (3**19 + 1, False),
        (-3, False),
    ]

    all_passed = True
    for idx, (n, expected) in enumerate(test_cases):
        try:
            result = solution.isPowerOfThree(n)
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
# 27\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

# @lcpr case=start
# 9\n
# @lcpr case=end

# @lcpr case=start
# 45\n
# @lcpr case=end

#
