#
# @lc app=leetcode.cn id=239 lang=python3
# @lcpr version=30203
#
# [239] 滑动窗口最大值
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from collections import deque
from common.node import *


# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        result = []

        for i, num in enumerate(nums):
            while queue and queue[0] <= i - k:
                queue.popleft()
            while queue and nums[queue[-1]] <= num:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                result.append(nums[queue[0]])

        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.maxSlidingWindow, ([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]),
        (solution.maxSlidingWindow, ([1], 1), [1]),
        (solution.maxSlidingWindow, ([9, 11], 2), [11]),
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
# [1,3,-1,-3,5,3,6,7]\n3\n
# @lcpr case=end
