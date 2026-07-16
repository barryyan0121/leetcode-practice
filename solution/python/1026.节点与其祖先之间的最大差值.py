#
# @lc app=leetcode.cn id=1026 lang=python3
#
# [1026] 节点与其祖先之间的最大差值
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from common.node import TreeNode


# @lc code=start
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def difference(node, smallest, largest):
            if not node:
                return largest - smallest
            smallest = min(smallest, node.val)
            largest = max(largest, node.val)
            return max(
                difference(node.left, smallest, largest),
                difference(node.right, smallest, largest),
            )

        return difference(root, root.val, root.val)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.maxAncestorDiff,
            (TreeNode.create_root([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]),),
            7,
        ),
        (
            solution.maxAncestorDiff,
            (TreeNode.create_root([1, None, 2, None, 0, 3]),),
            3,
        ),
        (solution.maxAncestorDiff, (TreeNode.create_root([5]),), 0),
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
