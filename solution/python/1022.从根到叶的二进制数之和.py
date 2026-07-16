#
# @lc app=leetcode.cn id=1022 lang=python3
#
# [1022] 从根到叶的二进制数之和
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from common.node import TreeNode


# @lc code=start
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def total(node, value):
            if not node:
                return 0
            value = value * 2 + node.val
            if not node.left and not node.right:
                return value
            return total(node.left, value) + total(node.right, value)

        return total(root, 0)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.sumRootToLeaf, (TreeNode.create_root([1, 0, 1, 0, 1, 0, 1]),), 22),
        (solution.sumRootToLeaf, (TreeNode.create_root([0]),), 0),
        (solution.sumRootToLeaf, (TreeNode.create_root([1]),), 1),
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
