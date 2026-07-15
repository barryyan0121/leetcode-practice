#
# @lc app=leetcode.cn id=799 lang=python3
#
# [799] 香槟塔
#

import os
import sys


# @lc code=start
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [float(poured)]
        for _ in range(query_row):
            next_row = [0.0] * (len(glasses) + 1)
            for index, amount in enumerate(glasses):
                overflow = max(0.0, (amount - 1) / 2)
                next_row[index] += overflow
                next_row[index + 1] += overflow
            glasses = next_row
        return min(1.0, glasses[query_glass])


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.champagneTower, (1, 1, 1), 0.0),
        (solution.champagneTower, (2, 1, 1), 0.5),
        (solution.champagneTower, (100000009, 33, 17), 1.0),
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
