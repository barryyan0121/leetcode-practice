# @lc app=leetcode.cn id=1372 lang=python3

from typing import Optional

from common.node import TreeNode


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> tuple[int, int, int]:
            if not node:
                return -1, -1, -1
            left_info = dfs(node.left) if node.left else (-1, -1, -1)
            right_info = dfs(node.right) if node.right else (-1, -1, -1)
            left = left_info[1] + 1
            right = right_info[0] + 1
            return left, right, max(left_info[2], right_info[2], left, right)

        return dfs(root)[2]


if __name__ == "__main__":
    test_cases = [
        (
            Solution().longestZigZag,
            (
                TreeNode.create_root(
                    [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1]
                ),
            ),
            3,
        )
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1372 题 "最长 ZigZag 路径" 所有测试用例通过')
