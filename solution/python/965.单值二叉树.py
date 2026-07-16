#
# @lc app=leetcode.cn id=965 lang=python3
#
# [965] 单值二叉树
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from common.node import TreeNode


# @lc code=start
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        value = root.val
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val != value:
                return False
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return True


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.isUnivalTree,
            (TreeNode.create_root([1, 1, 1, 1, 1, None, 1]),),
            True,
        ),
        (solution.isUnivalTree, (TreeNode.create_root([2, 2, 2, 5, 2]),), False),
        (solution.isUnivalTree, (TreeNode.create_root([7]),), True),
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
