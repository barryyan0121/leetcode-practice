#
# @lc app=leetcode.cn id=236 lang=python3
# @lcpr version=30202
#
# [236] 二叉树的最近公共祖先
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    root1 = TreeNode.create_root([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p1 = root1.left
    q1 = root1.right
    expected1 = TreeNode.create_root([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])

    root2 = TreeNode.create_root([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p2 = root2.left
    q2 = root2.left.right.right
    expected2 = TreeNode.create_root([5, 6, 2, None, None, 7, 4])

    test_cases = [
        (solution.lowestCommonAncestor, (root1, p1, q1), expected1),
        (solution.lowestCommonAncestor, (root2, p2, q2), expected2),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            result_str = TreeNode.print_tree(result) if result else "null"
            expected_str = TreeNode.print_tree(expected) if expected else "null"
            assert result_str == expected_str
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result_str}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected_str}, 实际 = {result_str}"
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
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n1\n
# @lcpr case=end
