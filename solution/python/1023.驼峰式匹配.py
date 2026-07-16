#
# @lc app=leetcode.cn id=1023 lang=python3
#
# [1023] 驼峰式匹配
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def matches(query):
            index = 0
            for letter in query:
                if index < len(pattern) and letter == pattern[index]:
                    index += 1
                elif letter.isupper():
                    return False
            return index == len(pattern)

        return [matches(query) for query in queries]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.camelMatch,
            (
                ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
                "FB",
            ),
            [True, False, True, True, False],
        ),
        (
            solution.camelMatch,
            (
                ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
                "FoBa",
            ),
            [True, False, True, False, False],
        ),
        (solution.camelMatch, (["a", "A"], "a"), [True, False]),
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
