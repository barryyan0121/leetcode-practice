#
# @lc app=leetcode.cn id=988 lang=python3
#
# [988] 从叶结点开始的最小字符串
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from common.node import TreeNode


# @lc code=start
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        smallest = None
        path = []

        def visit(node):
            nonlocal smallest
            path.append(chr(ord("a") + node.val))
            if not node.left and not node.right:
                candidate = "".join(reversed(path))
                if smallest is None or candidate < smallest:
                    smallest = candidate
            if node.left:
                visit(node.left)
            if node.right:
                visit(node.right)
            path.pop()

        visit(root)
        return smallest


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.smallestFromLeaf,
            (TreeNode.create_root([0, 1, 2, 3, 4, 3, 4]),),
            "dba",
        ),
        (
            solution.smallestFromLeaf,
            (TreeNode.create_root([25, 1, 3, 1, 3, 0, 2]),),
            "adz",
        ),
        (solution.smallestFromLeaf, (TreeNode.create_root([0]),), "a"),
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
