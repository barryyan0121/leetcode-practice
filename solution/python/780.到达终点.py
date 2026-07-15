#
# @lc app=leetcode.cn id=780 lang=python3
#
# [780] 到达终点
#

import os
import sys


# @lc code=start
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        return (
            tx == sx
            and ty >= sy
            and (ty - sy) % tx == 0
            or ty == sy
            and tx >= sx
            and (tx - sx) % ty == 0
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.reachingPoints, (1, 1, 3, 5), True),
        (solution.reachingPoints, (1, 1, 2, 2), False),
        (solution.reachingPoints, (1, 1, 1, 1), True),
        (solution.reachingPoints, (9, 10, 9, 19), True),
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
