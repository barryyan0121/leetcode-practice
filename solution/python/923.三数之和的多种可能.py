#
# @lc app=leetcode.cn id=923 lang=python3
#
# [923] 三数之和的多种可能
#

import os
import sys
from collections import Counter
from typing import List


# @lc code=start
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        seen = Counter()
        answer = 0
        for middle, number in enumerate(arr):
            for right in range(middle + 1, len(arr)):
                answer += seen[target - number - arr[right]]
            seen[number] += 1
        return answer % (10**9 + 7)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.threeSumMulti, ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8), 20),
        (solution.threeSumMulti, ([1, 1, 2, 2, 2, 2], 5), 12),
        (solution.threeSumMulti, ([0, 0, 0], 0), 1),
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
