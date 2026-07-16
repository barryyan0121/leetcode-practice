#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        next_pop = 0
        for value in pushed:
            stack.append(value)
            while stack and stack[-1] == popped[next_pop]:
                stack.pop()
                next_pop += 1
        return not stack


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.validateStackSequences, ([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]), True),
        (solution.validateStackSequences, ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]), False),
        (solution.validateStackSequences, ([], []), True),
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
