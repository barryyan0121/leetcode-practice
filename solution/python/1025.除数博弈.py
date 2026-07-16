#
# @lc app=leetcode.cn id=1025 lang=python3
#
# [1025] 除数博弈
#

import os
import sys


# @lc code=start
class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.divisorGame, (2,), True),
        (solution.divisorGame, (3,), False),
        (solution.divisorGame, (4,), True),
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
