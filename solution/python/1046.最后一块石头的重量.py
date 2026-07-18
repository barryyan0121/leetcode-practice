import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            first, second = -heapq.heappop(heap), -heapq.heappop(heap)
            if first != second:
                heapq.heappush(heap, second - first)
        return -heap[0] if heap else 0


if __name__ == "__main__":
    test_cases = [([2, 7, 4, 1, 8, 1], 1), ([1], 1), ([2, 2], 0)]
    for _, (stones, expected) in enumerate(test_cases):
        assert Solution().lastStoneWeight(stones) == expected
