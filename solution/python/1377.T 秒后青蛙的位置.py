# @lc app=leetcode.cn id=1377 lang=python3
from collections import defaultdict
from typing import List


class Solution:
    def frogPosition(
        self, n: int, edges: List[List[int]], t: int, target: int
    ) -> float:
        graph = defaultdict(list)
        for left, right in edges:
            graph[left].append(right)
            graph[right].append(left)

        def dfs(node: int, parent: int, time: int, probability: float) -> float:
            children = [child for child in graph[node] if child != parent]
            if time == t:
                return probability if node == target else 0.0
            if not children:
                return probability if node == target else 0.0
            if node == target:
                return 0.0
            share = probability / len(children)
            return max(
                (dfs(child, node, time + 1, share) for child in children), default=0.0
            )

        return dfs(1, 0, 0, 1.0)


if __name__ == "__main__":
    test_cases = [
        (
            Solution().frogPosition,
            (7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 2, 4),
            1 / 6,
        ),
        (Solution().frogPosition, (3, [[2, 1], [3, 2]], 1, 2), 1.0),
    ]
    for _, (func, args, expected) in enumerate(test_cases):
        assert func(*args) == expected
    print('第 1377 题 "T 秒后青蛙的位置" 所有测试用例通过')
