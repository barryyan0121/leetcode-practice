#
# @lc app=leetcode.cn id=98 lang=python3
# @lcpr version=30202
#
# [98] 验证二叉搜索树
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import TreeNode


# @lc code=start
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        current = root
        prev = None

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            if prev is not None and current.val <= prev:
                return False
            prev = current.val
            current = current.right

        return True


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.isValidBST, (TreeNode.create_root([2, 1, 3]),), True),
        (
            solution.isValidBST,
            (TreeNode.create_root([5, 1, 4, None, None, 3, 6]),),
            False,
        ),
        (solution.isValidBST, (TreeNode.create_root([2, 2, 2]),), False),
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
# [2,1,3]\n
# @lcpr case=end
