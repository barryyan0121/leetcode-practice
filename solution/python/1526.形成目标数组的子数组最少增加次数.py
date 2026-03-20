#
# @lc app=leetcode.cn id=1526 lang=python3
# @lcpr version=30300
#
# [1526] 形成目标数组的子数组最少增加次数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = target[0]
        for i in range(1, len(target)):
            ans += max(0, target[i] - target[i - 1])
        return ans


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.minNumberOperations, ([1, 2, 3, 2, 1],), 3),
        (solution.minNumberOperations, ([3, 1, 1, 2],), 4),
        (solution.minNumberOperations, ([3, 1, 5, 4, 2],), 7),
        (solution.minNumberOperations, ([1, 1, 1, 1],), 1),
        (solution.minNumberOperations, ([5],), 5),
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
# [1,2,3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [3,1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,1,5,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1]\n
# @lcpr case=end

#
