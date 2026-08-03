# @lc app=leetcode.cn id=1367 lang=python3

from typing import Optional

from common.node import ListNode, TreeNode


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True

        def match(node: Optional[TreeNode], current: Optional[ListNode]) -> bool:
            if not current:
                return True
            if not node or node.val != current.val:
                return False
            return match(node.left, current.next) or match(node.right, current.next)

        return bool(root) and (
            match(root, head)
            or self.isSubPath(head, root.left)
            or self.isSubPath(head, root.right)
        )


if __name__ == "__main__":
    test_cases = [
        (
            Solution().isSubPath,
            (
                ListNode.create_head([4, 2, 8]),
                TreeNode.create_root([1, 4, 4, None, 2, 2, None, 1, None, 6, 8]),
            ),
            True,
        )
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1367 题 "二叉树中的链表" 所有测试用例通过')
