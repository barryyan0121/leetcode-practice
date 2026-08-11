#
# @lc app=leetcode.cn id=2281 lang=python3
# @lcpr version=30203
#
# [2281] 巫师的总力量和
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        mod = 10**9 + 7
        n = len(strength)
        prefix = [0]
        for value in strength:
            prefix.append(prefix[-1] + value)
        prefix_of_prefix = [0]
        for value in prefix:
            prefix_of_prefix.append(prefix_of_prefix[-1] + value)

        left = [-1] * n
        stack = []
        for i, value in enumerate(strength):
            while stack and strength[stack[-1]] >= value:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        answer = 0
        for i, value in enumerate(strength):
            left_count = i - left[i]
            right_count = right[i] - i
            right_sum = prefix_of_prefix[right[i] + 1] - prefix_of_prefix[i + 1]
            left_sum = prefix_of_prefix[i + 1] - prefix_of_prefix[left[i] + 1]
            answer += value * (right_sum * left_count - left_sum * right_count)
        return answer % mod


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.totalStrength, ([1, 3, 1, 2],), 44),
        (solution.totalStrength, ([5, 4, 6],), 213),
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
    print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
    sys.exit(1)
