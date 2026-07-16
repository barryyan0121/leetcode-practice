#
# @lc app=leetcode.cn id=987 lang=python3
#
# [987] 二叉树的垂序遍历
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from common.node import TreeNode


# @lc code=start
class Solution:
    def verticalTraversal(self, root: TreeNode):
        nodes = []

        def visit(node, row, column):
            if not node:
                return
            nodes.append((column, row, node.val))
            visit(node.left, row + 1, column - 1)
            visit(node.right, row + 1, column + 1)

        visit(root, 0, 0)
        result = []
        previous_column = None
        for column, _, value in sorted(nodes):
            if column != previous_column:
                result.append([])
                previous_column = column
            result[-1].append(value)
        return result


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.verticalTraversal,
            (TreeNode.create_root([3, 9, 20, None, None, 15, 7]),),
            [[9], [3, 15], [20], [7]],
        ),
        (
            solution.verticalTraversal,
            (TreeNode.create_root([1, 2, 3, 4, 5, 6, 7]),),
            [[4], [2], [1, 5, 6], [3], [7]],
        ),
        (solution.verticalTraversal, (TreeNode.create_root([1]),), [[1]]),
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
