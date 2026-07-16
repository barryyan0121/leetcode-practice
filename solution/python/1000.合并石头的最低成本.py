#
# @lc app=leetcode.cn id=1000 lang=python3
#
# [1000] 合并石头的最低成本
#

import os
import sys
from itertools import accumulate
from typing import List


# @lc code=start
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        size = len(stones)
        if (size - 1) % (k - 1):
            return -1
        prefix = [0, *accumulate(stones)]
        dp = [[0] * size for _ in range(size)]
        for length in range(2, size + 1):
            for left in range(size - length + 1):
                right = left + length - 1
                dp[left][right] = min(
                    dp[left][middle] + dp[middle + 1][right]
                    for middle in range(left, right, k - 1)
                )
                if (length - 1) % (k - 1) == 0:
                    dp[left][right] += prefix[right + 1] - prefix[left]
        return dp[0][-1]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.mergeStones, ([3, 2, 4, 1], 2), 20),
        (solution.mergeStones, ([3, 2, 4, 1], 3), -1),
        (solution.mergeStones, ([3, 5, 1, 2, 6], 3), 25),
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
