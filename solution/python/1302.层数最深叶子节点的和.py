# @lc app=leetcode.cn id=1302 lang=python3

from typing import Optional

from common.node import TreeNode


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        level = [root]
        while level:
            next_level = [
                child for node in level for child in (node.left, node.right) if child
            ]
            if not next_level:
                return sum(node.val for node in level)
            level = next_level
        return 0


if __name__ == "__main__":
    test_cases = [
        (
            Solution().deepestLeavesSum,
            (
                TreeNode.create_root(
                    [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]
                ),
            ),
            15,
        ),
        (
            Solution().deepestLeavesSum,
            (
                TreeNode.create_root(
                    [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5]
                ),
            ),
            19,
        ),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1302 题 "层数最深叶子节点的和" 所有测试用例通过')
