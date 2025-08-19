#
# @lc app=leetcode.cn id=1394 lang=python3
# @lcpr version=30202
#
# [1394] 找出数组中的幸运数
#

import sys
import os

from collections import Counter

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import List
from common.node import *


# @lc code=start
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        for num in sorted(counter.keys(), reverse=True):
            if counter[num] == num:
                return num
        return -1
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.findLucky, ([2, 2, 3, 4],), 2),
        (solution.findLucky, ([1, 2, 2, 3, 3, 3],), 3),
        (solution.findLucky, ([2, 2, 2, 3, 3],), -1),
        (solution.findLucky, ([5],), -1),
        (solution.findLucky, ([7, 7, 7, 7, 7, 7, 7],), 7),
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
# [2,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,3,3,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,3,3]\n
# @lcpr case=end

# @lcpr case=start
# [5]\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7,7,7,7]\n
# @lcpr case=end

#
