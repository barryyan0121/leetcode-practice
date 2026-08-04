"""3486. 最长特殊路径 II"""

import heapq
import sys


class Solution:
    def longestSpecialPath(self, edges: list[list[int]], nums: list[int]) -> list[int]:
        velontrida = (edges, nums)
        n = len(nums)
        graph = [[] for _ in range(n)]
        for left, right, length in edges:
            graph[left].append((right, length))
            graph[right].append((left, length))

        last = {}
        second = {}
        third = {}
        versions = {}
        second_heap = []
        third_heap = []
        prefix = [0]
        best_length = 0
        best_nodes = 1

        def top_two_second_positions() -> tuple[int, int]:
            while second_heap and second_heap[0][2] != versions.get(
                second_heap[0][1], 0
            ):
                heapq.heappop(second_heap)
            if not second_heap:
                return -1, -1
            first = heapq.heappop(second_heap)
            while second_heap and second_heap[0][2] != versions.get(
                second_heap[0][1], 0
            ):
                heapq.heappop(second_heap)
            second_best = -second_heap[0][0] if second_heap else -1
            heapq.heappush(second_heap, first)
            return -first[0], second_best

        def top_third_position() -> int:
            while third_heap and third_heap[0][2] != versions.get(third_heap[0][1], 0):
                heapq.heappop(third_heap)
            return -third_heap[0][0] if third_heap else -1

        def dfs(node: int, parent: int, depth: int) -> None:
            nonlocal best_length, best_nodes
            value = nums[node]
            old_last = last.get(value, -1)
            old_second = second.get(value, -1)
            old_third = third.get(value, -1)
            version = versions.get(value, 0) + 1
            versions[value] = version
            third[value] = old_second
            second[value] = old_last
            last[value] = depth
            if old_last >= 0:
                heapq.heappush(second_heap, (-old_last, value, version))
            if old_second >= 0:
                heapq.heappush(third_heap, (-old_second, value, version))

            _, second_largest = top_two_second_positions()
            start = max(second_largest, top_third_position()) + 1
            length = prefix[depth] - prefix[start]
            nodes = depth - start + 1
            if length > best_length:
                best_length, best_nodes = length, nodes
            elif length == best_length:
                best_nodes = min(best_nodes, nodes)

            for child, edge_length in graph[node]:
                if child == parent:
                    continue
                prefix.append(prefix[-1] + edge_length)
                dfs(child, node, depth + 1)
                prefix.pop()

            version = versions.get(value, 0) + 1
            versions[value] = version
            if old_second >= 0:
                heapq.heappush(second_heap, (-old_second, value, version))
            if old_third >= 0:
                heapq.heappush(third_heap, (-old_third, value, version))
            if old_last >= 0:
                last[value] = old_last
            else:
                last.pop(value, None)
            if old_second >= 0:
                second[value] = old_second
            else:
                second.pop(value, None)
            if old_third >= 0:
                third[value] = old_third
            else:
                third.pop(value, None)

        sys.setrecursionlimit(max(1000, n * 2 + 10))
        dfs(0, -1, 0)
        return [best_length, best_nodes]


if __name__ == "__main__":
    test_cases = [
        (
            (
                [
                    [0, 1, 1],
                    [1, 2, 3],
                    [1, 3, 1],
                    [2, 4, 6],
                    [4, 7, 2],
                    [3, 5, 2],
                    [3, 6, 5],
                    [6, 8, 3],
                ],
                [1, 1, 0, 3, 1, 2, 1, 1, 0],
            ),
            [9, 3],
        ),
        (([[1, 0, 3], [0, 2, 4], [0, 3, 5]], [1, 1, 0, 2]), [5, 2]),
    ]
    for _, ((edges, nums), expected) in enumerate(test_cases):
        assert Solution().longestSpecialPath(edges, nums) == expected
