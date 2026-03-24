#
# @lc app=leetcode.cn id=133 lang=python3
# @lcpr version=30203
#
# [133] 克隆图
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


class Node:
    def __init__(self, val: int = 0, neighbors: List["Node"] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# @lc code=start
class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None

        clones = {}

        def dfs(curr: "Node") -> "Node":
            if curr in clones:
                return clones[curr]

            copy = Node(curr.val)
            clones[curr] = copy
            copy.neighbors = [dfs(nei) for nei in curr.neighbors]
            return copy

        return dfs(node)


# @lc code=end


if __name__ == "__main__":
    solution = Solution()

    def build_graph(adj_list: List[List[int]]) -> Optional[Node]:
        if not adj_list:
            return None
        nodes = [Node(i + 1) for i in range(len(adj_list))]
        for i, neighbors in enumerate(adj_list):
            nodes[i].neighbors = [nodes[j - 1] for j in neighbors]
        return nodes[0]

    def serialize_graph(node: Optional[Node]) -> List[List[int]]:
        if node is None:
            return []
        result = []
        visited = set()
        queue = [node]
        while queue:
            curr = queue.pop(0)
            if curr in visited:
                continue
            visited.add(curr)
            result.append([curr.val] + [nei.val for nei in curr.neighbors])
            for nei in curr.neighbors:
                if nei not in visited:
                    queue.append(nei)
        result.sort()
        return result

    # 测试用例 (func, args, result)
    test_cases = [
        (
            solution.cloneGraph,
            (build_graph([[2, 4], [1, 3], [2, 4], [1, 3]]),),
            [[1, 2, 4], [2, 1, 3], [3, 2, 4], [4, 1, 3]],
        ),
        (
            solution.cloneGraph,
            (build_graph([[2], [1]]),),
            [[1, 2], [2, 1]],
        ),
        (solution.cloneGraph, (None,), []),
    ]

    all_passed = True
    for idx, (func, args, expected) in enumerate(test_cases):
        try:
            result = func(*args)
            result = serialize_graph(result)
            assert result == expected
            print(f"测试用例 {idx + 1} 通过: n = {args}, result = {result}")
        except AssertionError:
            all_passed = False
            print(
                f"测试用例 {idx + 1} 失败: n = {args}, 期望 = {expected}, 实际 = {result}"
            )

    file_path = os.path.basename(__file__).split(".")
    file_number = file_path[0]
    file_name = file_path[1]
    if all_passed:
        print(f'第 {file_number} 题 "{file_name}" 所有测试用例通过')
        sys.exit(0)
    else:
        print(f'第 {file_number} 题 "{file_name}" 部分测试用例失败')
        sys.exit(1)


#
# @lcpr case=start
# [[2,4],[1,3],[2,4],[1,3]]\n
# @lcpr case=end
