#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找共用字符
#

import os
import sys
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])
        for word in words[1:]:
            common &= Counter(word)
        return list(common.elements())


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.commonChars, (["bella", "label", "roller"],), ["e", "l", "l"]),
        (solution.commonChars, (["cool", "lock", "cook"],), ["c", "o"]),
        (solution.commonChars, (["a", "b"],), []),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert sorted(result) == sorted(expected)
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
