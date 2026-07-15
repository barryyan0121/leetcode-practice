#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

import os
import sys
from typing import *


# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {character: index for index, character in enumerate(s)}
        answer = []
        start = end = 0
        for index, character in enumerate(s):
            end = max(end, last[character])
            if index == end:
                answer.append(end - start + 1)
                start = index + 1
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.partitionLabels, ("ababcbacadefegdehijhklij",), [9, 7, 8]),
        (solution.partitionLabels, ("eccbbbbdec",), [10]),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
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
