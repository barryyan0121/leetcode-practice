#
# @lc app=leetcode.cn id=131 lang=python3
# @lcpr version=30203
#
# [131] 分割回文串
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start: int) -> None:
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start, len(s)):
                if not is_palindrome(start, end):
                    continue
                path.append(s[start : end + 1])
                backtrack(end + 1)
                path.pop()

        backtrack(0)
        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def normalize(parts: List[List[str]]) -> List[List[str]]:
        return sorted(parts)

    # 测试用例 (func, args, result)
    test_cases = [
        (solution.partition, ("aab",), [["a", "a", "b"], ["aa", "b"]]),
        (solution.partition, ("a",), [["a"]]),
        (solution.partition, ("efe",), [["e", "f", "e"], ["efe"]]),
    ]

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
# "aab"\n
# @lcpr case=end
