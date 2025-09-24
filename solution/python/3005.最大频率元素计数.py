#
# @lc app=leetcode.cn id=3005 lang=python3
# @lcpr version=30203
#
# [3005] 最大频率元素计数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *
from collections import Counter


# @lc code=start
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        max_freq = max(cnt.values())
        return max_freq * sum(1 for v in cnt.values() if v == max_freq)
        # @lc code=end
        pass


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.maxFrequencyElements, ([1, 2, 2, 3, 1, 4],), 4),
        (solution.maxFrequencyElements, ([1, 2, 3, 4, 5],), 5),
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
# [1,2,2,3,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

#
