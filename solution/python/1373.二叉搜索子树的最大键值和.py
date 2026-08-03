# @lc app=leetcode.cn id=1373 lang=python3

from typing import Optional

from common.node import TreeNode


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        best = 0

        def dfs(node: Optional[TreeNode]):
            nonlocal best
            if not node:
                return True, 0, float("inf"), float("-inf")
            left_valid, left_sum, left_min, left_max = dfs(node.left)
            right_valid, right_sum, right_min, right_max = dfs(node.right)
            valid = left_valid and right_valid and left_max < node.val < right_min
            total = left_sum + right_sum + node.val
            if valid:
                best = max(best, total)
            return valid, total, min(left_min, node.val), max(right_max, node.val)

        dfs(root)
        return best


if __name__ == "__main__":
    test_cases = [
        (Solution().maxSumBST, (TreeNode.create_root([2, 1, 3]),), 6),
        (Solution().maxSumBST, (TreeNode.create_root([4, 3, None, 1, 2]),), 2),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1373 题 "二叉搜索子树的最大键值和" 所有测试用例通过')
