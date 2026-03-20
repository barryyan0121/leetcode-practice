#
# @lc app=leetcode.cn id=3289 lang=python3
# @lcpr version=30300
#
# [3289] 数字小镇中的捣蛋鬼
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1
            if count[x] == 2:
                res.append(x)
        return res


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.getSneakyNumbers, ([0, 1, 1, 0],), [1, 0]),
        (solution.getSneakyNumbers, ([0, 3, 2, 1, 3, 2],), [3, 2]),
        (solution.getSneakyNumbers, ([7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2],), [4, 5]),
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
# [0,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,2,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [7,1,5,4,3,4,6,0,9,5,8,2]\n
# @lcpr case=end

#
