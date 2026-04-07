#
# @lc app=leetcode.cn id=235 lang=python3
# @lcpr version=30202
#
# [235] 二叉搜索树的最近公共祖先
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
        if p.val > q.val:
            p, q = q, p

        while root:
            if q.val < root.val:
                root = root.left
            elif p.val > root.val:
                root = root.right
            else:
                return root


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    root1 = TreeNode.create_root([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p1 = root1.left
    q1 = root1.left.right
    expected1 = TreeNode.create_root([2, 0, 4, None, None, 3, 5])

    root2 = TreeNode.create_root([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p2 = root2.left
    q2 = root2.right
    expected2 = TreeNode.create_root([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])

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
# [6,2,8,0,4,7,9,null,null,3,5]\n2\n8\n
# @lcpr case=end
