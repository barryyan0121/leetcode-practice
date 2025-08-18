#
# @lc app=leetcode.cn id=679 lang=python3
# @lcpr version=30202
#
# [679] 24 点游戏
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import List
from common.node import *

# @lc code=start
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        TARGET = 24
        EPSILON = 1e-6
        ADD, MULTIPLY, SUBTRACT, DIVIDE = 0, 1, 2, 3

        def solve(nums: List[float]) -> bool:
            if not nums:
                return False
            if len(nums) == 1:
                return abs(nums[0] - TARGET) < EPSILON
            for i, x in enumerate(nums):
                for j, y in enumerate(nums):
                    if i != j:
                        newNums = list()
                        for k, z in enumerate(nums):
                            if k != i and k != j:
                                newNums.append(z)
                        for k in range(4):
                            if k < 2 and i > j:
                                continue
                            if k == ADD:
                                newNums.append(x + y)
                            elif k == MULTIPLY:
                                newNums.append(x * y)
                            elif k == SUBTRACT:
                                newNums.append(x - y)
                            elif k == DIVIDE:
                                if abs(y) < EPSILON:
                                    continue
                                newNums.append(x / y)
                            if solve(newNums):
                                return True
                            newNums.pop()
            return False

        return solve(cards)

# @lc code=end


if __name__ == '__main__':
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.judgePoint24, ([4, 1, 8, 7],), True),
        (solution.judgePoint24, ([1, 2, 1, 2],), False),
        (solution.judgePoint24, ([1, 3, 4, 6],), True)
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}")

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
# [4, 1, 8, 7]\n
# @lcpr case=end

# @lcpr case=start
# [1, 2, 1, 2]\n
# @lcpr case=end

#

