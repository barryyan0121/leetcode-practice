#
# @lc app=leetcode.cn id=2467 lang=python3
# @lcpr version=30203
#
# [2467] 树上最大得分和路径
#

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from typing import *
from common.node import *


# @lc code=start
class Solution:
    def mostProfitablePath(
        self, edges: List[List[int]], bob: int, amount: List[int]
    ) -> int:
        n = len(amount)
        graph = [[] for _ in range(n)]
        for left, right in edges:
            graph[left].append(right)
            graph[right].append(left)

        parent = [-1] * n
        depth = [0] * n
        order = [0]
        for node in order:
            for neighbor in graph[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    depth[neighbor] = depth[node] + 1
                    order.append(neighbor)

        bob_time = [n] * n
        node = bob
        time = 0
        while node != -1:
            bob_time[node] = time
            node = parent[node]
            time += 1

        answer = -(10**30)
        stack = [(0, -1, 0, 0)]
        while stack:
            node, previous, time, score = stack.pop()
            if time < bob_time[node]:
                score += amount[node]
            elif time == bob_time[node]:
                score += amount[node] // 2
            children = [neighbor for neighbor in graph[node] if neighbor != previous]
            if not children:
                answer = max(answer, score)
            else:
                stack.extend((child, node, time + 1, score) for child in children)
        return answer


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    assert (
        solution.mostProfitablePath(
            [[0, 1], [1, 2], [1, 3], [3, 4]], 3, [-2, 4, 2, -4, 6]
        )
        == 6
    )
    assert solution.mostProfitablePath([[0, 1]], 1, [-7280, 2350]) == -7280
    print("测试用例通过")
