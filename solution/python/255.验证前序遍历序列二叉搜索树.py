#
# @lc app=leetcode.cn id=255 lang=python3
# @lcpr version=30203
#
# [255] 验证前序遍历序列二叉搜索树
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        lower = float("-inf")
        for num in preorder:
            if num < lower:
                return False
            while stack and num > stack[-1]:
                lower = stack.pop()
            stack.append(num)
        return True


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.verifyPreorder, [[5, 2, 1, 3, 6]], True),
        (solution.verifyPreorder, [[5, 2, 6, 1, 3]], False),
        (solution.verifyPreorder, [[]], True),
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
# [5,2,1,3,6]\n
# @lcpr case=end

#
