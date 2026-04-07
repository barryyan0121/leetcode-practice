#
# @lc app=leetcode.cn id=451 lang=python3
# @lcpr version=30203
#
# [451] 根据字符出现频率排序
#

import sys
import os
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        return "".join(char * count for char, count in counts.most_common())


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def check_result(actual: str, expected_options: List[str]) -> bool:
        return actual in expected_options

    test_cases = [
        (solution.frequencySort, ("tree",), ["eetr", "eert"]),
        (solution.frequencySort, ("cccaaa",), ["cccaaa", "aaaccc"]),
        (solution.frequencySort, ("Aabb",), ["bbAa", "bbaA"]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert check_result(result, expected)
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}")

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
# "tree"\n
# @lcpr case=end
