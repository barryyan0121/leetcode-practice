#
# @lc app=leetcode.cn id=654 lang=python3
# @lcpr version=30203
#
# [654] 最大二叉树
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import TreeNode


# @lc code=start
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        idx = nums.index(max(nums))
        root = TreeNode(nums[idx])
        root.left = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx + 1 :])
        return root


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.constructMaximumBinaryTree,
            ([3, 2, 1, 6, 0, 5],),
            "6,3,null,2,null,1,null,null,5,0,null,null,null",
        ),
        (
            solution.constructMaximumBinaryTree,
            ([3, 2, 1],),
            "3,null,2,null,1,null,null",
        ),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = TreeNode.print_tree(func(*args))
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
