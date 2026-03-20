#
# @lc app=leetcode.cn id=3318 lang=python3
# @lcpr version=30300
#
# [3318] 计算子数组的 x-sum I
#

import sys
import os
from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        for left in range(len(nums) - k + 1):
            window = nums[left : left + k]
            cnt = Counter(window)
            items = sorted(cnt.items(), key=lambda p: (-p[1], -p[0]))
            total = 0
            for value, freq in items[:x]:
                total += value * freq
            ans.append(total)
        return ans


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.findXSum, ([1, 1, 2, 2, 3, 4, 2, 3], 6, 2), [6, 10, 12]),
        (solution.findXSum, ([3, 8, 7, 8, 7, 5], 2, 2), [11, 15, 15, 15, 12]),
        (solution.findXSum, ([5, 5, 5], 3, 1), [15]),
        (solution.findXSum, ([1, 2, 3, 4], 2, 1), [2, 3, 4]),
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
# [1,1,2,2,3,4,2,3]\n6\n2\n
# @lcpr case=end

# @lcpr case=start
# [3,8,7,8,7,5]\n2\n2\n
# @lcpr case=end

#
