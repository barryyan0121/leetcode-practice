#
# @lc app=leetcode.cn id=40 lang=python3
# @lcpr version=30202
#
# [40] 组合总和 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []

        def backtrack(start: int, total: int) -> None:
            if total == target:
                result.append(path.copy())
                return

            prev = None
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                if prev == candidate:
                    continue
                new_total = total + candidate
                if new_total > target:
                    break
                prev = candidate
                path.append(candidate)
                backtrack(i + 1, new_total)
                path.pop()

        backtrack(0, 0)
        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.combinationSum2,
            ([10, 1, 2, 7, 6, 1, 5], 8),
            [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]],
        ),
        (solution.combinationSum2, ([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]]),
        (solution.combinationSum2, ([1, 1, 1, 1], 2), [[1, 1]]),
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
# [10,1,2,7,6,1,5]\n8\n
# @lcpr case=end

#
