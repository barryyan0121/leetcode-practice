from heapq import heapify, heappop, heappush


class Solution:
    def connectSticks(self, sticks: list[int]) -> int:
        heapify(sticks)
        total = 0
        while len(sticks) > 1:
            merged = heappop(sticks) + heappop(sticks)
            total += merged
            heappush(sticks, merged)
        return total


if __name__ == "__main__":
    test_cases = [([2, 4, 3], 14), ([1, 8, 3, 5], 30)]
    for _, (sticks, expected) in enumerate(test_cases):
        assert Solution().connectSticks(sticks) == expected
