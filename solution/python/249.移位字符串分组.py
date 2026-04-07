#
# @lc app=leetcode.cn id=249 lang=python3
# @lcpr version=30203
#
# [249] 移位字符串分组
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from collections import defaultdict
from common.node import *


# @lc code=start
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strings:
            if len(s) == 1:
                key = ("single",)
            else:
                diffs = []
                for i in range(1, len(s)):
                    diffs.append((ord(s[i]) - ord(s[i - 1])) % 26)
                key = tuple(diffs)
            groups[key].append(s)
        return list(groups.values())
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.groupStrings,
            [["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]],
            [["abc", "bcd", "xyz"], ["az", "ba"], ["acef"], ["a", "z"]],
        ),
        (solution.groupStrings, [["a"]], [["a"]]),
    ]

    def normalize(groups: List[List[str]]) -> List[List[str]]:
        return sorted([sorted(group) for group in groups])

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
# ["abc","bcd","acef","xyz","az","ba","a","z"]\n
# @lcpr case=end

#
