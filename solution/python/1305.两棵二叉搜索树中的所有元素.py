# @lc app=leetcode.cn id=1305 lang=python3

from typing import List, Optional

from common.node import TreeNode


class Solution:
    def getAllElements(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> List[int]:
        def inorder(root: Optional[TreeNode]) -> List[int]:
            result, stack = [], []
            while stack or root:
                while root:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                result.append(root.val)
                root = root.right
            return result

        first, second = inorder(root1), inorder(root2)
        result = []
        i = j = 0
        while i < len(first) or j < len(second):
            if j == len(second) or (i < len(first) and first[i] <= second[j]):
                result.append(first[i])
                i += 1
            else:
                result.append(second[j])
                j += 1
        return result


if __name__ == "__main__":
    test_cases = [
        (
            Solution().getAllElements,
            (TreeNode.create_root([2, 1, 4]), TreeNode.create_root([1, 0, 3])),
            [0, 1, 1, 2, 3, 4],
        ),
        (
            Solution().getAllElements,
            (TreeNode.create_root([1, None, 8]), TreeNode.create_root([8, 1])),
            [1, 1, 8, 8],
        ),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1305 题 "两棵二叉搜索树中的所有元素" 所有测试用例通过')
