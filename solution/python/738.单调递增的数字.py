#
# @lc app=leetcode.cn id=738 lang=python3
# @lcpr version=30202
#
# [738] 单调递增的数字
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = list(str(n))
        for i in range(len(s) - 1):
            if s[i] > s[i + 1]:
                # 向左回退处理连续相同字符 (如 332 → 299)
                while i > 0 and s[i] == s[i - 1]:
                    i -= 1
                s[i] = str(int(s[i]) - 1)
                s[i + 1 :] = "9" * (len(s) - i - 1)  # 后面全部置为9
                return int("".join(s))
        return int("".join(s))
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.monotoneIncreasingDigits, (10,), 9),
        (solution.monotoneIncreasingDigits, (1234,), 1234),
        (solution.monotoneIncreasingDigits, (332,), 299),
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
# 10\n
# @lcpr case=end

# @lcpr case=start
# 1234\n
# @lcpr case=end

# @lcpr case=start
# 332\n
# @lcpr case=end

#
