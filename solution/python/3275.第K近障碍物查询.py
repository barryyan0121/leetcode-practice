import heapq


class Solution:
    def resultsArray(self, queries: list[list[int]], k: int) -> list[int]:
        nearest = []
        answer = []
        for x, y in queries:
            distance = abs(x) + abs(y)
            heapq.heappush(nearest, -distance)
            if len(nearest) > k:
                heapq.heappop(nearest)
            answer.append(-nearest[0] if len(nearest) == k else -1)
        return answer


if __name__ == "__main__":
    test_cases = [
        (([[1, 2], [3, 4], [2, 3], [-3, 0]], 2), [-1, 7, 5, 3]),
        (([[5, 5], [4, 4], [3, 3]], 1), [10, 8, 6]),
    ]
    for _, ((queries, k), expected) in enumerate(test_cases):
        assert Solution().resultsArray(queries, k) == expected
