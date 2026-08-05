"""2203. 包含要求路径的最小带权子图"""

import heapq


class Solution:
    def minimumWeight(
        self,
        n: int,
        edges: list[list[int]],
        src1: int,
        src2: int,
        dest: int,
    ) -> int:
        graph = [[] for _ in range(n)]
        reverse = [[] for _ in range(n)]
        for start, end, weight in edges:
            graph[start].append((end, weight))
            reverse[end].append((start, weight))

        def distances(start: int, adjacency: list[list[tuple[int, int]]]) -> list[int]:
            result = [float("inf")] * n
            result[start] = 0
            heap = [(0, start)]
            while heap:
                distance, node = heapq.heappop(heap)
                if distance != result[node]:
                    continue
                for neighbor, weight in adjacency[node]:
                    candidate = distance + weight
                    if candidate < result[neighbor]:
                        result[neighbor] = candidate
                        heapq.heappush(heap, (candidate, neighbor))
            return result

        first = distances(src1, graph)
        second = distances(src2, graph)
        to_dest = distances(dest, reverse)
        answer = min(
            (first[node] + second[node] + to_dest[node] for node in range(n)),
            default=float("inf"),
        )
        return -1 if answer == float("inf") else answer


if __name__ == "__main__":
    test_cases = [
        (
            (
                6,
                [
                    [0, 2, 2],
                    [0, 5, 6],
                    [1, 0, 3],
                    [1, 4, 5],
                    [2, 1, 1],
                    [2, 3, 3],
                    [3, 4, 2],
                    [4, 5, 1],
                ],
                0,
                1,
                5,
            ),
            9,
        )
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumWeight(*args) == expected
