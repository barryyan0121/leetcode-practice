# @lc app=leetcode.cn id=1719 lang=python3


class Solution:
    def checkWays(self, pairs: list[list[int]]) -> int:
        neighbors = {}
        for left, right in pairs:
            neighbors.setdefault(left, set()).add(right)
            neighbors.setdefault(right, set()).add(left)
        root = next(
            (
                node
                for node, adjacent in neighbors.items()
                if len(adjacent) == len(neighbors) - 1
            ),
            None,
        )
        if root is None:
            return 0
        result = 1
        for node, adjacent in neighbors.items():
            if node == root:
                continue
            parent = None
            parent_degree = len(neighbors) + 1
            for candidate in adjacent:
                if (
                    len(neighbors[candidate]) >= len(adjacent)
                    and len(neighbors[candidate]) < parent_degree
                ):
                    parent, parent_degree = candidate, len(neighbors[candidate])
            if parent is None or not adjacent - {parent} <= neighbors[parent]:
                return 0
            if parent_degree == len(adjacent):
                result = 2
        return result


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (solution.checkWays, ([[1, 2], [2, 3]],), 1),
        (solution.checkWays, ([[1, 2], [2, 3], [1, 3]],), 2),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1719 题 "重构一棵树的方案数" 所有测试用例通过')
