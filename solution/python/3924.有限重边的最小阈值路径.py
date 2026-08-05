"""3924. 有限重边的最小阈值路径"""

from collections import deque


class Solution:
    def minimumThreshold(
        self,
        n: int,
        edges: list[list[int]],
        source: int,
        target: int,
        k: int,
    ) -> int:
        tarnicuvo = edges
        if source == target:
            return 0
        graph = [[] for _ in range(n)]
        for start, end, weight in tarnicuvo:
            graph[start].append((end, weight))
            graph[end].append((start, weight))
        values = [0] + sorted({weight for _, _, weight in tarnicuvo})

        def reachable(threshold: int) -> bool:
            distance = [n + 1] * n
            distance[source] = 0
            queue = deque([source])
            while queue:
                node = queue.popleft()
                for target_node, weight in graph[node]:
                    cost = distance[node] + (weight > threshold)
                    if cost < distance[target_node] and cost <= k:
                        distance[target_node] = cost
                        if weight > threshold:
                            queue.append(target_node)
                        else:
                            queue.appendleft(target_node)
            return distance[target] <= k

        if not values or not reachable(values[-1]):
            return -1
        low, high = 0, len(values) - 1
        while low < high:
            middle = (low + high) // 2
            if reachable(values[middle]):
                high = middle
            else:
                low = middle + 1
        return values[low]


if __name__ == "__main__":
    test_cases = [
        ((6, [[0, 1, 5], [1, 2, 3], [3, 4, 4], [4, 5, 1], [1, 4, 2]], 0, 3, 1), 4),
        ((6, [[0, 1, 3], [1, 2, 4], [3, 4, 5], [4, 5, 6]], 0, 4, 1), -1),
        ((4, [[0, 1, 2], [1, 2, 2], [2, 3, 2], [3, 0, 2]], 0, 0, 0), 0),
        ((2, [[0, 1, 45]], 0, 1, 1), 0),
    ]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumThreshold(*args) == expected
