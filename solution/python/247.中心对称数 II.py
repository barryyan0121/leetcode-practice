#
# @lc app=leetcode.cn id=247 lang=python3
# @lcpr version=30203
#
# [247] 中心对称数 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def build(length: int, total: int) -> List[str]:
            if length == 0:
                return [""]
            if length == 1:
                return ["0", "1", "8"]
            res = []
            for mid in build(length - 2, total):
                for a, b in [("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]:
                    if length == total and a == "0":
                        continue
                    res.append(a + mid + b)
            return res

        return build(n, n)
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.findStrobogrammatic, [1], ["0", "1", "8"]),
        (solution.findStrobogrammatic, [2], ["11", "69", "88", "96"]),
        (solution.findStrobogrammatic, [3], ["101", "609", "808", "906", "111", "619", "818", "916", "181", "689", "888", "986"]),
    ]

    def normalize(res: List[str]) -> List[str]:
        return sorted(res)

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert normalize(result) == normalize(expected)
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

#
