from collections import defaultdict
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
        current = next(
            value for value, neighbors in graph.items() if len(neighbors) == 1
        )
        result = []
        previous = None
        for _ in range(len(graph)):
            result.append(current)
            next_values = [value for value in graph[current] if value != previous]
            previous, current = current, next_values[0] if next_values else None
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.restoreArray([[2, 1], [3, 4], [3, 2]]) in (
        [1, 2, 3, 4],
        [4, 3, 2, 1],
    )
    print("1743 passed")
