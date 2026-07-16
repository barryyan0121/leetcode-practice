#
# @lc app=leetcode.cn id=887 lang=python3
#
# [887] 鸡蛋掉落
#

import os
import sys


# @lc code=start
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        floors = [0] * (k + 1)
        moves = 0
        while floors[k] < n:
            moves += 1
            for eggs in range(k, 0, -1):
                floors[eggs] += floors[eggs - 1] + 1
        return moves


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.superEggDrop, (1, 2), 2),
        (solution.superEggDrop, (2, 6), 3),
        (solution.superEggDrop, (3, 14), 4),
        (solution.superEggDrop, (2, 100), 14),
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
