#
# @lc app=leetcode.cn id=935 lang=python3
#
# [935] 骑士拨号器
#

import os
import sys


# @lc code=start
class Solution:
    def knightDialer(self, n: int) -> int:
        moves = (
            (4, 6),
            (6, 8),
            (7, 9),
            (4, 8),
            (0, 3, 9),
            (),
            (0, 1, 7),
            (2, 6),
            (1, 3),
            (2, 4),
        )
        modulo = 10**9 + 7
        counts = [1] * 10
        for _ in range(n - 1):
            counts = [
                sum(counts[neighbor] for neighbor in moves[digit]) % modulo
                for digit in range(10)
            ]
        return sum(counts) % modulo


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.knightDialer, (1,), 10),
        (solution.knightDialer, (2,), 20),
        (solution.knightDialer, (3131,), 136006598),
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
