#
# @lc app=leetcode.cn id=829 lang=python3
#
# [829] 连续整数求和
#

import os
import sys


# @lc code=start
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        answer = 0
        length = 1
        while length * (length + 1) // 2 <= n:
            answer += (n - length * (length - 1) // 2) % length == 0
            length += 1
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.consecutiveNumbersSum, (5,), 2),
        (solution.consecutiveNumbersSum, (9,), 3),
        (solution.consecutiveNumbersSum, (15,), 4),
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
