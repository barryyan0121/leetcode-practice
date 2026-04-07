#
# @lc app=leetcode.cn id=222 lang=python3
# @lcpr version=30203
#
# [222] 完全二叉树的节点个数
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import TreeNode


# @lc code=start
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_height = 0
        right_height = 0
        left = root
        right = root

        while left is not None:
            left_height += 1
            left = left.left

        while right is not None:
            right_height += 1
            right = right.right

        if left_height == right_height:
            return (1 << left_height) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (solution.countNodes, (TreeNode.create_root([1, 2, 3, 4, 5, 6]),), 6),
        (solution.countNodes, (TreeNode.create_root([]),), 0),
        (solution.countNodes, (TreeNode.create_root([1]),), 1),
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
# [1,2,3,4,5,6]\n
# @lcpr case=end
