#
# @lc app=leetcode.cn id=3894 lang=python3
#
# [3894] 交通信号灯颜色
#

import os
import sys


# @lc code=start
class Solution:
    def trafficSignal(self, timer: int) -> str:
        if timer == 0:
            return "Green"
        if timer == 30:
            return "Orange"
        if 30 < timer <= 90:
            return "Red"
        return "Invalid"


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.trafficSignal, (60,), "Red"),
        (solution.trafficSignal, (5,), "Invalid"),
        (solution.trafficSignal, (0,), "Green"),
        (solution.trafficSignal, (30,), "Orange"),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: args = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: args = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
