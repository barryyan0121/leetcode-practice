#
# @lc app=leetcode.cn id=951 lang=python3
#
# [951] 翻转等价二叉树
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from common.node import TreeNode


# @lc code=start
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 or not root2:
            return root1 is root2
        if root1.val != root2.val:
            return False
        return (
            self.flipEquiv(root1.left, root2.left)
            and self.flipEquiv(root1.right, root2.right)
        ) or (
            self.flipEquiv(root1.left, root2.right)
            and self.flipEquiv(root1.right, root2.left)
        )


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.flipEquiv,
            (
                TreeNode.create_root([1, 2, 3, 4, 5, 6, None, None, None, 7, 8]),
                TreeNode.create_root(
                    [1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7]
                ),
            ),
            True,
        ),
        (solution.flipEquiv, (None, None), True),
        (
            solution.flipEquiv,
            (TreeNode.create_root([0]), TreeNode.create_root([1])),
            False,
        ),
    ]
    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        result = func(*args)
        try:
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )
    file_path = os.path.basename(__file__).split(".")
    if all_passed:
        print(f'第 {file_path[0]} 题 "{file_path[1]}" 所有测试用例通过')
        sys.exit(0)
    sys.exit(1)
