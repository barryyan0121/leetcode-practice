# @lc app=leetcode.cn id=1530 lang=python3


class Solution:
    def countPairs(self, root, distance: int) -> int:
        result = 0

        def visit(node):
            nonlocal result
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            left = visit(node.left)
            right = visit(node.right)
            result += sum(
                first + second <= distance for first in left for second in right
            )
            return [value + 1 for value in left + right if value + 1 < distance]

        visit(root)
        return result


if __name__ == "__main__":

    class Node:
        def __init__(self, left=None, right=None):
            self.left = left
            self.right = right

    solution = Solution()
    test_cases = [(solution.countPairs, (Node(Node(), Node()), 2), 1)]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1530 题 "好叶子节点对的数量" 所有测试用例通过')
