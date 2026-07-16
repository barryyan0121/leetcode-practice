#
# @lc app=leetcode.cn id=993 lang=python3
#
# [993] 二叉树的堂兄弟节点
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from common.node import TreeNode


# @lc code=start
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        found = {}
        stack = [(root, None, 0)]
        while stack and len(found) < 2:
            node, parent, depth = stack.pop()
            if node.val in (x, y):
                found[node.val] = (parent, depth)
            if node.left:
                stack.append((node.left, node, depth + 1))
            if node.right:
                stack.append((node.right, node, depth + 1))
        return found[x][1] == found[y][1] and found[x][0] is not found[y][0]


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.isCousins, (TreeNode.create_root([1, 2, 3, 4]), 4, 3), False),
        (
            solution.isCousins,
            (TreeNode.create_root([1, 2, 3, None, 4, None, 5]), 5, 4),
            True,
        ),
        (solution.isCousins, (TreeNode.create_root([1, 2, 3, None, 4]), 2, 3), False),
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
