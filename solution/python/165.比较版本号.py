#
# @lc app=leetcode.cn id=165 lang=python3
# @lcpr version=30203
#
# [165] 比较版本号
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_list = version1.split(".")
        v2_list = version2.split(".")
        n1, n2 = len(v1_list), len(v2_list)
        for i in range(max(n1, n2)):
            v1 = int(v1_list[i]) if i < n1 else 0
            v2 = int(v2_list[i]) if i < n2 else 0
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        return 0
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.compareVersion, ("1.2", "1.10"), -1),
        (solution.compareVersion, ("1.01", "1.001"), 0),
        (solution.compareVersion, ("1.0", "1.0.0.0"), 0),
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
# "1.2"\n"1.10"\n
# @lcpr case=end

# @lcpr case=start
# "1.01"\n"1.001"\n
# @lcpr case=end

# @lcpr case=start
# "1.0"\n"1.0.0.0"\n
# @lcpr case=end

#
