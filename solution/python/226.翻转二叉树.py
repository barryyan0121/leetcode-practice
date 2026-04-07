#
# @lc app=leetcode.cn id=226 lang=python3
# @lcpr version=30203
#
# [226] 翻转二叉树
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import TreeNode


# @lc code=start
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.invertTree,
            (TreeNode.create_root([4, 2, 7, 1, 3, 6, 9]),),
            "4,7,9,null,null,6,null,null,2,3,null,null,1,null,null",
        ),
        (
            solution.invertTree,
            (TreeNode.create_root([2, 1, 3]),),
            "2,3,null,null,1,null,null",
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            actual = TreeNode.print_tree(result)
            assert actual == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {actual}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {actual}"
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
# [4,2,7,1,3,6,9]\n
# @lcpr case=end
