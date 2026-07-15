#
# @lc app=leetcode.cn id=818 lang=python3
#
# [818] 赛车
#

import os
import sys
from functools import cache


# @lc code=start
class Solution:
    def racecar(self, target: int) -> int:
        @cache
        def moves(distance: int) -> int:
            accelerations = distance.bit_length()
            full_distance = (1 << accelerations) - 1
            if distance == full_distance:
                return accelerations
            answer = accelerations + 1 + moves(full_distance - distance)
            previous_distance = (1 << (accelerations - 1)) - 1
            for reverse_accelerations in range(accelerations - 1):
                remaining = (
                    distance - previous_distance + (1 << reverse_accelerations) - 1
                )
                answer = min(
                    answer,
                    accelerations + reverse_accelerations + 1 + moves(remaining),
                )
            return answer

        return moves(target)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.racecar, (3,), 2),
        (solution.racecar, (6,), 5),
        (solution.racecar, (1,), 1),
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
