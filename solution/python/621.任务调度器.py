#
# @lc app=leetcode.cn id=621 lang=python3
# @lcpr version=30203
#
# [621] 任务调度器
#

import sys
import os
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks).values()
        max_count = max(counts)
        max_count_tasks = sum(count == max_count for count in counts)
        return max(len(tasks), (max_count - 1) * (n + 1) + max_count_tasks)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.leastInterval, (["A", "A", "A", "B", "B", "B"], 2), 8),
        (solution.leastInterval, (["A", "A", "A", "B", "B", "B"], 0), 6),
        (
            solution.leastInterval,
            (["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2),
            16,
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
