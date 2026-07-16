#
# @lc app=leetcode.cn id=907 lang=python3
#
# [907] 子数组的最小值之和
#

import os
import sys
from typing import List


# @lc code=start
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        ending_sum = 0
        answer = 0
        for value in arr:
            count = 1
            while stack and stack[-1][0] >= value:
                previous, previous_count = stack.pop()
                ending_sum -= previous * previous_count
                count += previous_count
            stack.append((value, count))
            ending_sum += value * count
            answer += ending_sum
        return answer % 1_000_000_007


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.sumSubarrayMins, ([3, 1, 2, 4],), 17),
        (solution.sumSubarrayMins, ([11, 81, 94, 43, 3],), 444),
        (solution.sumSubarrayMins, ([1, 1],), 3),
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
