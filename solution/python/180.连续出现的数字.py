#
# @lc app=leetcode.cn id=180 lang=python3
# @lcpr version=30203
#
# [180] 连续出现的数字
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def consecutiveNumbers(self, logs: List[List[int]]) -> List[int]:
        logs = sorted(logs, key=lambda x: x[0])
        result = set()
        run_num = None
        run_len = 0
        prev_id = None

        for log_id, num in logs:
            if prev_id is not None and log_id == prev_id + 1 and num == run_num:
                run_len += 1
            else:
                run_num = num
                run_len = 1
            if run_len >= 3:
                result.add(run_num)
            prev_id = log_id

        return sorted(result)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.consecutiveNumbers,
            ([[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2], [8, 2]],),
            [1, 2],
        ),
        (
            solution.consecutiveNumbers,
            ([[1, 1], [2, 2], [3, 3]],),
            [],
        ),
        (
            solution.consecutiveNumbers,
            ([[1, 5], [2, 5], [3, 5], [4, 5]],),
            [5],
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)


#
# @lcpr case=start
# [[1,1],[2,1],[3,1],[4,2],[5,1],[6,2],[7,2],[8,2]]\n
# @lcpr case=end
