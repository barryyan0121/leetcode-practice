import sys


class Solution:
    def longestSpecialPath(self, edges: list[list[int]], nums: list[int]) -> list[int]:
        zemorvitho = (edges, nums)
        graph = [[] for _ in nums]
        for source, target, length in edges:
            graph[source].append((target, length))
            graph[target].append((source, length))

        sys.setrecursionlimit(max(1000000, len(nums) * 2))
        last = {}
        distances = []
        answer_length, answer_nodes = 0, 1

        def visit(node: int, parent: int, distance: int, left: int) -> None:
            nonlocal answer_length, answer_nodes
            position = len(distances)
            previous = last.get(nums[node], -1)
            next_left = max(left, previous + 1)
            last[nums[node]] = position
            distances.append(distance)
            path_length = distance - distances[next_left]
            node_count = position - next_left + 1
            if path_length > answer_length:
                answer_length, answer_nodes = path_length, node_count
            elif path_length == answer_length:
                answer_nodes = min(answer_nodes, node_count)
            for child, edge_length in graph[node]:
                if child != parent:
                    visit(child, node, distance + edge_length, next_left)
            distances.pop()
            if previous == -1:
                del last[nums[node]]
            else:
                last[nums[node]] = previous

        visit(0, -1, 0, 0)
        return [answer_length, answer_nodes]


if __name__ == "__main__":
    test_cases = [
        (
            (
                [[0, 1, 2], [1, 2, 3], [1, 3, 5], [1, 4, 4], [2, 5, 6]],
                [2, 1, 2, 1, 3, 1],
            ),
            [6, 2],
        ),
        (([[1, 0, 8]], [2, 2]), [0, 1]),
    ]
    for _, ((edges, nums), expected) in enumerate(test_cases):
        assert Solution().longestSpecialPath(edges, nums) == expected
