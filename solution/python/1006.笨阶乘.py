#
# @lc app=leetcode.cn id=1006 lang=python3
#
# [1006] 笨阶乘
#

import os
import sys


# @lc code=start
class Solution:
    def clumsy(self, n: int) -> int:
        stack = [n]
        for offset, value in enumerate(range(n - 1, 0, -1)):
            operation = offset % 4
            if operation == 0:
                stack[-1] *= value
            elif operation == 1:
                stack[-1] = int(stack[-1] / value)
            elif operation == 2:
                stack.append(value)
            else:
                stack.append(-value)
        return sum(stack)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.clumsy, (4,), 7),
        (solution.clumsy, (10,), 12),
        (solution.clumsy, (1,), 1),
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
