#
# @lc app=leetcode.cn id=830 lang=python3
#
# [830] 较大分组的位置
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        answer = []
        start = 0
        for end in range(len(s)):
            if end == len(s) - 1 or s[end] != s[end + 1]:
                if end - start >= 2:
                    answer.append([start, end])
                start = end + 1
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.largeGroupPositions, ("abbxxxxzzy",), [[3, 6]]),
        (solution.largeGroupPositions, ("abc",), []),
        (
            solution.largeGroupPositions,
            ("abcdddeeeeaabbbcd",),
            [[3, 5], [6, 9], [12, 14]],
        ),
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
