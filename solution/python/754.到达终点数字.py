#
# @lc app=leetcode.cn id=754 lang=python3
#
# [754] 到达终点数字
#

import os
import sys


# @lc code=start
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        step = distance = 0
        while distance < target or (distance - target) % 2:
            step += 1
            distance += step
        return step


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.reachNumber, (2,), 3),
        (solution.reachNumber, (3,), 2),
        (solution.reachNumber, (-4,), 3),
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
