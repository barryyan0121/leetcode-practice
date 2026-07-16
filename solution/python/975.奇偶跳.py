#
# @lc app=leetcode.cn id=975 lang=python3
#
# [975] 奇偶跳
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)

        def next_indices(order):
            result = [-1] * n
            stack = []
            for index in order:
                while stack and index > stack[-1]:
                    result[stack.pop()] = index
                stack.append(index)
            return result

        higher = next_indices(sorted(range(n), key=lambda index: (arr[index], index)))
        lower = next_indices(sorted(range(n), key=lambda index: (-arr[index], index)))
        odd = [False] * n
        even = [False] * n
        odd[-1] = even[-1] = True
        for index in range(n - 2, -1, -1):
            if higher[index] != -1:
                odd[index] = even[higher[index]]
            if lower[index] != -1:
                even[index] = odd[lower[index]]
        return sum(odd)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.oddEvenJumps, ([10, 13, 12, 14, 15],), 2),
        (solution.oddEvenJumps, ([2, 3, 1, 1, 4],), 3),
        (solution.oddEvenJumps, ([5, 1, 3, 4, 2],), 3),
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
