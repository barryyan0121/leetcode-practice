#
# @lc app=leetcode.cn id=108 lang=python3
# @lcpr version=30202
#
# [108] 将有序数组转换为二叉搜索树
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import TreeNode


# @lc code=start
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(nums) - 1)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def inorder(root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return inorder(root.left) + [root.val] + inorder(root.right)

    def height(root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(height(root.left), height(root.right)) + 1

    def is_balanced(root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return (
            abs(height(root.left) - height(root.right)) <= 1
            and is_balanced(root.left)
            and is_balanced(root.right)
        )

    # 测试用例 (func, args, result)
    test_cases = [
        (solution.sortedArrayToBST, ([-10, -3, 0, 5, 9],), [-10, -3, 0, 5, 9]),
        (solution.sortedArrayToBST, ([1, 3],), [1, 3]),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            assert inorder(result) == expected
            assert is_balanced(result)
            print(
                f"测试用例 {idx + 1} 通过: n = {args}, result = {TreeNode.print_tree(result)}"
            )
        except AssertionError:
            all_passed = False
            actual = inorder(result) if result is not None else []
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {actual}"
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
# [-10,-3,0,5,9]\n
# @lcpr case=end
