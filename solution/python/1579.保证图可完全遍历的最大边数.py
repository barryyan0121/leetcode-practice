# @lc app=leetcode.cn id=1579 lang=python3


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        class UnionFind:
            def __init__(self):
                self.parent = list(range(n + 1))
                self.count = n

            def find(self, x):
                while self.parent[x] != x:
                    self.parent[x] = self.parent[self.parent[x]]
                    x = self.parent[x]
                return x

            def union(self, a, b):
                a, b = self.find(a), self.find(b)
                if a == b:
                    return False
                self.parent[a] = b
                self.count -= 1
                return True

        alice, bob = UnionFind(), UnionFind()
        kept = 0
        for edge_type, a, b in edges:
            if edge_type == 3:
                used = alice.union(a, b) | bob.union(a, b)
                kept += used
        for edge_type, a, b in edges:
            if edge_type == 1:
                kept += alice.union(a, b)
            elif edge_type == 2:
                kept += bob.union(a, b)
        if alice.count != 1 or bob.count != 1:
            return -1
        return len(edges) - kept


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            solution.maxNumEdgesToRemove,
            (4, [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]),
            0,
        )
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1579 题 "保证图可完全遍历的最大边数" 所有测试用例通过')
