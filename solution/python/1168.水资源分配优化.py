#
# @lc app=leetcode.cn id=1168 lang=python3
#
# [1168] 水资源分配优化
#


# @lc code=start
class Solution:
    def minCostToSupplyWater(self, n, wells, pipes):
        parent = list(range(n + 1))

        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        cost = 0
        edges = pipes + [[0, house, price] for house, price in enumerate(wells, 1)]
        for left, right, price in sorted(edges, key=lambda edge: edge[2]):
            left, right = find(left), find(right)
            if left != right:
                parent[left] = right
                cost += price
        return cost


# @lc code=end


if __name__ == "__main__":
    test_cases = [
        ((3, [1, 2, 2], [[1, 2, 1], [2, 3, 1]]), 3),
        ((2, [1, 1], [[1, 2, 1]]), 2),
    ]
    for index, (args, expected) in enumerate(test_cases):
        assert Solution().minCostToSupplyWater(*args) == expected, index
