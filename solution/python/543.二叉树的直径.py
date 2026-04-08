#
# @lc app=leetcode.cn id=543 lang=python3
# @lcpr version=30203
#
# [543] 二叉树的直径
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import TreeNode


# @lc code=start
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def depth(node: Optional[TreeNode]) -> int:
            nonlocal best
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            best = max(best, left + right)
            return max(left, right) + 1

        depth(root)
        return best


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.diameterOfBinaryTree, (TreeNode.create_root([1, 2, 3, 4, 5]),), 3),
        (solution.diameterOfBinaryTree, (TreeNode.create_root([1, 2]),), 1),
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
# [1,2,3,4,5]\n
# @lcpr case=end
#
