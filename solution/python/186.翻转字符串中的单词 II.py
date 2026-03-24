#
# @lc app=leetcode.cn id=186 lang=python3
# @lcpr version=30203
#
# [186] 翻转字符串中的单词 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def reverse(left: int, right: int) -> None:
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        reverse(0, len(s) - 1)
        start = 0
        for i in range(len(s) + 1):
            if i == len(s) or s[i] == " ":
                reverse(start, i - 1)
                start = i + 1
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    arr1 = list("the sky is blue")
    arr2 = list("  hello world  ")
    arr3 = list("a")
    test_cases = [
        (solution.reverseWords, [arr1], None),
        (lambda: arr1, (), list("blue is sky the")),
        (solution.reverseWords, [arr2], None),
        (lambda: arr2, (), list("  world hello  ")),
        (solution.reverseWords, [arr3], None),
        (lambda: arr3, (), list("a")),
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
# ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]\n
# @lcpr case=end

# @lcpr case=start
# ["a"]\n
# @lcpr case=end

#
