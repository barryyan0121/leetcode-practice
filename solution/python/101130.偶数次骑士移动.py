#
# @lc app=leetcode.cn id=101130 lang=python3
#
# [101130] 偶数次骑士移动
#

import os
import sys


# @lc code=start
class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        return (sum(start) - sum(target)) % 2 == 0


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.canReach, ([1, 1], [2, 2]), True),
        (solution.canReach, ([4, 5], [6, 6]), False),
        (solution.canReach, ([0, 0], [7, 7]), True),
        (solution.canReach, ([0, 0], [0, 1]), False),
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
