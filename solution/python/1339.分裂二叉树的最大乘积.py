# @lc app=leetcode.cn id=1339 lang=python3

from typing import Optional

from common.node import TreeNode


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums = []

        def total(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            value = node.val + total(node.left) + total(node.right)
            sums.append(value)
            return value

        whole = total(root)
        return max(value * (whole - value) for value in sums) % (10**9 + 7)


if __name__ == "__main__":
    test_cases = [
        (Solution().maxProduct, (TreeNode.create_root([1, 2, 3, 4, 5, 6]),), 110),
        (
            Solution().maxProduct,
            (TreeNode.create_root([1, None, 2, 3, 4, None, None, 5, 6]),),
            90,
        ),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1339 题 "分裂二叉树的最大乘积" 所有测试用例通过')
