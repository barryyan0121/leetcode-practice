#
# @lc app=leetcode.cn id=248 lang=python3
# @lcpr version=30203
#
# [248] 中心对称数 III
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        pairs = [("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]

        def build(length: int, total: int) -> List[str]:
            if length == 0:
                return [""]
            if length == 1:
                return ["0", "1", "8"]
            res = []
            for mid in build(length - 2, total):
                for a, b in pairs:
                    if length == total and a == "0":
                        continue
                    res.append(a + mid + b)
            return res

        ans = 0
        for length in range(len(low), len(high) + 1):
            for s in build(length, length):
                if (len(s) == len(low) and s < low) or (len(s) == len(high) and s > high):
                    continue
                ans += 1
        return ans
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.strobogrammaticInRange, ["50", "100"], 3),
        (solution.strobogrammaticInRange, ["0", "0"], 1),
        (solution.strobogrammaticInRange, ["1", "1"], 1),
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
# "50"\n"100"\n
# @lcpr case=end

#
