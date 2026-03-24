#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index = {value: i for i, value in enumerate(inorder)}

        def build(in_left: int, in_right: int, post_left: int, post_right: int):
            if in_left > in_right:
                return None

            root_val = postorder[post_right]
            root = TreeNode(root_val)
            mid = index[root_val]
            left_size = mid - in_left

            root.left = build(in_left, mid - 1, post_left, post_left + left_size - 1)
            root.right = build(mid + 1, in_right, post_left + left_size, post_right - 1)
            return root

        return build(0, len(inorder) - 1, 0, len(postorder) - 1)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.buildTree,
            ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]),
            TreeNode.create_root([3, 9, 20, None, None, 15, 7]),
        ),
        (
            solution.buildTree,
            ([-1], [-1]),
            TreeNode.create_root([-1]),
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            result = TreeNode.print_tree(result) if result else "null"
            expected = TreeNode.print_tree(expected) if expected else "null"
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
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
# [9,3,15,20,7]\n[9,15,7,20,3]\n
# @lcpr case=end
