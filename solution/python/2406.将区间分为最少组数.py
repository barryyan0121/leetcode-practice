"""2406. 将区间分为最少组数"""

import heapq


class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        heap = []
        answer = 0
        for start, end in sorted(intervals):
            while heap and heap[0] < start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
            answer = max(answer, len(heap))
        return answer


if __name__ == "__main__":
    test_cases = [(([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]],), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minGroups(*args) == expected
