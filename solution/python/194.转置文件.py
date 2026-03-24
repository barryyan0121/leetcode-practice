#
# @lc app=leetcode.cn id=194 lang=python3
# @lcpr version=30203
#
# [194] 转置文件
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def transposeFile(self, lines: List[str]) -> List[str]:
        rows = [line.split() for line in lines]
        if not rows:
            return []
        return [" ".join(column) for column in zip(*rows)]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.transposeFile,
            (["name age", "alice 21", "ryan 30"],),
            ["name alice ryan", "age 21 30"],
        ),
        (
            solution.transposeFile,
            (["a b c", "d e f"],),
            ["a d", "b e", "c f"],
        ),
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
# lines = ["name age","alice 21","ryan 30"]\n
# @lcpr case=end
