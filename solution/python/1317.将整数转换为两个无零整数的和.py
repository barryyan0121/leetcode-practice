#
# @lc app=leetcode.cn id=1317 lang=python3
# @lcpr version=30202
#
# [1317] 将整数转换为两个无零整数的和
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for A in range(1, n):
            B = n - A
            if "0" not in str(A) + str(B):
                return [A, B]
        return []


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.getNoZeroIntegers, (2,), [1, 1]),
        (solution.getNoZeroIntegers, (11,), [2, 9]),
        (solution.getNoZeroIntegers, (10000,), [1, 9999]),
        (solution.getNoZeroIntegers, (69,), [1, 68]),
        (solution.getNoZeroIntegers, (1010,), [11, 999]),
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
# 2\n
# @lcpr case=end

# @lcpr case=start
# 11\n
# @lcpr case=end

# @lcpr case=start
# 10000\n
# @lcpr case=end

# @lcpr case=start
# 69\n
# @lcpr case=end

# @lcpr case=start
# 1010\n
# @lcpr case=end

#
