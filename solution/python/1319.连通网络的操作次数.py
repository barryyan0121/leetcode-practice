# @lc app=leetcode.cn id=1319 lang=python3

from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        parent = list(range(n))

        def find(node: int) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        components = n
        for left, right in connections:
            left_root, right_root = find(left), find(right)
            if left_root != right_root:
                parent[left_root] = right_root
                components -= 1
        return components - 1


if __name__ == "__main__":
    test_cases = [
        (Solution().makeConnected, (4, [[0, 1], [0, 2], [1, 2]]), 1),
        (Solution().makeConnected, (6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]), 2),
        (Solution().makeConnected, (6, [[0, 1], [0, 2], [0, 3], [1, 2]]), -1),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1319 题 "连通网络的操作次数" 所有测试用例通过')
