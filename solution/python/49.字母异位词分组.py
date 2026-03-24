#
# @lc app=leetcode.cn id=49 lang=python3
# @lcpr version=30202
#
# [49] 字母异位词分组
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def normalize(groups: List[List[str]]) -> List[List[str]]:
        return sorted([sorted(group) for group in groups])

    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.groupAnagrams,
            (["eat", "tea", "tan", "ate", "nat", "bat"],),
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        (solution.groupAnagrams, ([""],), [[""]]),
        (solution.groupAnagrams, (["a"],), [["a"]]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            normalized_result = normalize(result)
            normalized_expected = normalize(expected)
            assert normalized_result == normalized_expected
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
# ["eat","tea","tan","ate","nat","bat"]\n
# @lcpr case=end
