# @lc app=leetcode.cn id=1430 lang=python3

from collections import deque
from typing import List


class Solution:
    def isValidSequence(self, root: "TreeNode", arr: List[int]) -> bool:
        stack = [(root, 0)]
        while stack:
            node, index = stack.pop()
            if not node or node.val != arr[index]:
                continue
            if index == len(arr) - 1:
                if not node.left and not node.right:
                    return True
                continue
            stack.append((node.left, index + 1))
            stack.append((node.right, index + 1))
        return False


if __name__ == "__main__":

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def build_tree(values):
        if not values:
            return None
        root = TreeNode(values[0])
        nodes = deque([root])
        for left, right in zip(values[1::2], values[2::2]):
            node = nodes.popleft()
            if left is not None:
                node.left = TreeNode(left)
                nodes.append(node.left)
            if right is not None:
                node.right = TreeNode(right)
                nodes.append(node.right)
        return root

    root = build_tree([0, 1, 0, 0, 1, 0, None, None, 1, 0, 0])
    test_cases = [
        (Solution().isValidSequence, (root, [0, 1, 0, 1]), True),
        (Solution().isValidSequence, (root, [0, 0, 1]), False),
        (Solution().isValidSequence, (root, [0, 1, 1]), False),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1430 题 "判断给定的序列是否是二叉树从根到叶的路径" 所有测试用例通过')
