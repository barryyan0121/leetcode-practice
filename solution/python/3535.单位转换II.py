from collections import deque


class Solution:
    def queryConversions(
        self, conversions: list[list[int]], queries: list[list[int]]
    ) -> list[int]:
        modulus = 10**9 + 7
        size = len(conversions) + 1
        graph = [[] for _ in range(size)]
        for source, target, factor in conversions:
            factor %= modulus
            graph[source].append((target, factor))
            graph[target].append((source, pow(factor, modulus - 2, modulus)))

        from_root = [0] * size
        from_root[0] = 1
        queue = deque([0])
        while queue:
            node = queue.popleft()
            for neighbor, factor in graph[node]:
                if from_root[neighbor] == 0:
                    from_root[neighbor] = from_root[node] * factor % modulus
                    queue.append(neighbor)
        return [
            from_root[target] * pow(from_root[source], modulus - 2, modulus) % modulus
            for source, target in queries
        ]


if __name__ == "__main__":
    test_cases = [
        (([[0, 1, 2], [0, 2, 6]], [[1, 2], [1, 0]]), [3, 500000004]),
    ]
    for _, ((conversions, queries), expected) in enumerate(test_cases):
        assert Solution().queryConversions(conversions, queries) == expected
