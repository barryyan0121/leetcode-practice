# @lc app=leetcode.cn id=1609 lang=python3


class Solution:
    def isEvenOddTree(self, root) -> bool:
        from collections import deque

        queue = deque([root])
        level = 0
        while queue:
            previous = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.val % 2 != 1 - level % 2 or (
                    previous is not None
                    and (
                        node.val <= previous if level % 2 == 0 else node.val >= previous
                    )
                ):
                    return False
                previous = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return True


if __name__ == "__main__":

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val, self.left, self.right = val, left, right

    solution = Solution()
    tree = TreeNode(
        1, TreeNode(10, TreeNode(3), None), TreeNode(4, TreeNode(7), TreeNode(9))
    )
    test_cases = [(solution.isEvenOddTree, (tree,), True)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1609 题 "奇偶树" 所有测试用例通过')
